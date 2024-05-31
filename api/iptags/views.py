from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from .models import IpTag
from .serializers import IPTagSerializer, IPNetworkTagSerializer
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    View to render the home page with a form to input an IP address.

    URL pattern:
    - `/`

    Example:
        GET /
        Response: Renders home.html with a form to input an IP address.
    """
    template_name = 'home.html'


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


class IpTagListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to retrieve list of IpTag instances or create a new IpTag.

    Methods:
    - get: Retrieve a list of IpTag instances.
    - post: Create a new IpTag instance.

    URL pattern:
    - `ip-tags/`

    Example:
        GET /ip-tags/
        Response: [{"id": 1, "ip_network": "192.168.1.1", "tag": "example tag"}]

        POST /ip-tags/
        Request: {"ip_network": "192.168.1.2", "tag": "new tag"}
        Response: {"id": 2, "ip_network": "192.168.1.2", "tag": "new tag"}
    """
    queryset = IpTag.objects.all()
    serializer_class = IPNetworkTagSerializer


class IpTagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete an IpTag instance by ID.

    Methods:
    - get: Retrieve an IpTag instance by ID.
    - put: Update an IpTag instance by ID.
    - delete: Delete an IpTag instance by ID.

    URL pattern:
    - `ip-tags/<int:pk>/`

    Example:
        GET /ip-tags/1/
        Response: {"id": 1, "ip_network": "192.168.1.1", "tag": "example tag"}

        PUT /ip-tags/1/
        Request: {"ip_network": "192.168.1.1", "tag": "updated tag"}
        Response: {"id": 1, "ip_network": "192.168.1.1", "tag": "updated tag"}

        DELETE /ip-tags/1/
        Response: {"detail": "IpTag instance deleted."}
    """
    queryset = IpTag.objects.all()
    serializer_class = IPNetworkTagSerializer
