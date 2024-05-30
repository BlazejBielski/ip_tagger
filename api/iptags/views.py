from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import IpTag
from .pagination import CustomPagination
from .serializers import IPTagSerializer, IPNetworkTagSerializer
from django.shortcuts import render


class IpTagView(APIView):
    """
    API view to retrieve IpTag instances by IP address.

    Methods:
    - get: Retrieve IpTag instances filtered by the given IP address.

    URL pattern:
    - `ip-tags/<str:ip>/`

    Example:
        GET /ip-tags/192.168.1.1/
        Response: [{"id": 1, "ip_network": "192.168.1.1", "tag": "example tag"}]
    """
    def get(self, request, ip):
        try:
            ip_tags = IpTag.objects.filter(ip_network=ip)
            serializer = IPTagSerializer(ip_tags, many=True)
            flat_tags = [item for sublist in serializer.data for item in sublist]
            return JsonResponse(flat_tags, safe=False)
        except IpTag.DoesNotExist:
            return JsonResponse([], safe=False)


class IpTagReportView(APIView):
    """
       API view to generate a report for a given IP address.

       Methods:
       - get: Generate and return a report for the given IP address.

       URL pattern:
       - `ip-tags-report/<str:ip>/`

       Example:
           GET /ip-tags-report/192.168.1.1/
           Response: {"report": "This is a report for IP: 192.168.1.1"}
       """
    def get(self, request, ip):
        try:
            ip_tags = IpTag.objects.filter(ip_network=ip)
            tags = [tag.tag for tag in ip_tags]
            context = {'ip': ip, 'tags': tags}
            return render(request, 'ip_tag_report.html', context)
        except IpTag.DoesNotExist:
            return render(request, 'ip_tag_report.html', {'ip': ip, 'tags': []})


class IPTagRetrieveAPIView(APIView):
    """
        API view to retrieve a single IpTag instance by ID.

        Methods:
        - get: Retrieve an IpTag instance by ID.

        URL pattern:
        - `ip-tags/retrieve/<int:id>/`

        Example:
            GET /ip-tags/retrieve/1/
            Response: {"id": 1, "ip_network": "192.168.1.1", "tag": "example tag"}
        """
    def get(self, request, ip):
        ip_tags = IpTag.objects.filter(ip_network=ip)
        serializer = IPTagSerializer(ip_tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IPTagListView(ListAPIView):
    """
    API view to list all IpTag instances.

    Methods:
    - get: Return a list of all IpTag instances.

    URL pattern:
    - `ip-tags/list/`

    Example:
        GET /ip-tags/list/
        Response: [{"id": 1, "ip_network": "192.168.1.1", "tag": "example tag"}, ...]
    """
    serializer_class = IPNetworkTagSerializer
    queryset = IpTag.objects.all()
    pagination_class = CustomPagination


class IPTagCreateView(CreateAPIView):
    """
    API view to create a new IpTag instance.

    Methods:
    - post: Create a new IpTag instance.

    URL pattern:
    - `ip-tags/create/`

    Example:
        POST /ip-tags/create/
        Request body: {"ip_network": "192.168.1.1", "tag": "example tag"}
        Response: {"id": 1, "ip_network": "192.168.1.1", "tag": "example tag"}
    """
    serializer_class = IPTagSerializer
    queryset = IpTag.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class IPTagUpdateView(UpdateAPIView):
    """
        API view to update an existing IpTag instance.

        Methods:
        - put: Update an IpTag instance.
        - patch: Partially update an IpTag instance.

        URL pattern:
        - `ip-tags/update/<int:id>/`

        Example:
            PUT /ip-tags/update/1/
            Request body: {"ip_network": "192.168.1.2", "tag": "updated tag"}
            Response: {"id": 1, "ip_network": "192.168.1.2", "tag": "updated tag"}

            PATCH /ip-tags/update/1/
            Request body: {"tag": "partially updated tag"}
            Response: {"id": 1, "ip_network": "192.168.1.2", "tag": "partially updated tag"}
        """
    serializer_class = IPTagSerializer
    queryset = IpTag.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IPTagDeleteView(DestroyAPIView):
    """
        API view to delete an existing IpTag instance.

        Methods:
        - delete: Delete an IpTag instance.

        URL pattern:
        - `ip-tags/delete/<int:id>/`

        Example:
            DELETE /ip-tags/delete/1/
            Response: 204 No Content
        """
    serializer_class = IPTagSerializer
    queryset = IpTag.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
