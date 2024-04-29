from rest_framework import serializers

from .models import IpTag


class IPTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpTag
        fields = ['tag']
