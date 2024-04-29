from rest_framework import serializers

from .models import IpTag


class IPTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpTag
        fields = ['tag']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation['tag'].split(", ")