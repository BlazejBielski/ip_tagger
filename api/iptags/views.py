from rest_framework import generics

from .models import IpTag
from .serializers import IPTagSerializer


class IPTagsListView(generics.RetrieveAPIView):
    queryset = IpTag.objects.all()
    serializer_class = IPTagSerializer
