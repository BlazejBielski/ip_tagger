from django.http import JsonResponse
from rest_framework.views import APIView
from .models import IpTag
from .serializers import IPTagSerializer
from django.http import HttpResponse
from django.shortcuts import render


class IpTagView(APIView):
    def get(self, request, ip):
        try:
            ip_tags = IpTag.objects.filter(ip_network=ip)
            serializer = IPTagSerializer(ip_tags, many=True)
            flat_tags = [item for sublist in serializer.data for item in sublist]  # Spłaszcz listę
            return JsonResponse(flat_tags, safe=False)
        except IpTag.DoesNotExist:
            return JsonResponse([], safe=False)


class IpTagReportView(APIView):
    def get(self, request, ip):
        try:
            ip_tags = IpTag.objects.filter(ip_network=ip)
            tags = [tag.tag for tag in ip_tags]
            context = {'ip': ip, 'tags': tags}
            return render(request, 'ip_tag_report.html', context)
        except IpTag.DoesNotExist:
            return render(request, 'ip_tag_report.html', {'ip': ip, 'tags': []})
