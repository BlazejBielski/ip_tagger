from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import IpTag
from .pagination import CustomPagination
from .serializers import IPTagSerializer
from django.shortcuts import render


class IpTagView(APIView):
    def get(self, request, ip):
        try:
            ip_tags = IpTag.objects.filter(ip_network=ip)
            serializer = IPTagSerializer(ip_tags, many=True)
            flat_tags = [item for sublist in serializer.data for item in sublist]
            return JsonResponse(flat_tags, safe=False)
        except IpTag.DoesNotExist:
            return JsonResponse([], safe=False)


class IPTagRetrieveAPIView(APIView):
    def get(self, request, ip):
        ip_tags = IpTag.objects.filter(ip_network=ip)
        serializer = IPTagSerializer(ip_tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IPTagListView(ListAPIView):
    serializer_class = IPTagSerializer
    queryset = IpTag.objects.all()
    pagination_class = CustomPagination


class IPTagCreateView(CreateAPIView):
    serializer_class = IPTagSerializer
    queryset = IpTag.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class IPTagUpdateView(UpdateAPIView):
    serializer_class = IPTagSerializer
    queryset = IpTag.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IPTagDeleteView(DestroyAPIView):
    serializer_class = IPTagSerializer
    queryset = IpTag.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class IpTagReportView(APIView):
    def get(self, request, ip):
        try:
            ip_tags = IpTag.objects.filter(ip_network=ip)
            tags = [tag.tag for tag in ip_tags]
            context = {'ip': ip, 'tags': tags}
            return render(request, 'ip_tag_report.html', context)
        except IpTag.DoesNotExist:
            return render(request, 'ip_tag_report.html', {'ip': ip, 'tags': []})
