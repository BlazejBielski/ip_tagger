from rest_framework import serializers

from .models import IpTag


class IPTagSerializer(serializers.Serializer):
    class Meta:
        model = IpTag
        fields = '__all__'
