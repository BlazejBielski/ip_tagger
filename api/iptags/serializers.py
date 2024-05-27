from rest_framework import serializers

from .models import IpTag


class IPTagSerializer(serializers.ModelSerializer):
    """Serializer for tags from IpTag model.

    :returns: IPTagSerializer
    :rtype: rest_framework.serializers.Serializer

    """
    class Meta:
        model = IpTag
        fields = ['tag']

    def to_representation(self, instance):
        """function for split tags
        :param instance: serializer instance
        :return: representation of serializer instance
        """
        representation = super().to_representation(instance)
        return representation['tag'].split(", ")


class IPNetworkTagSerializer(serializers.ModelSerializer):
    """Serializer for IpTag model with IP and tags.

    :returns: IPTagSerializer
    :rtype: rest_framework.serializers.Serializer

    """
    class Meta:
        model = IpTag
        fields = ['id', 'ip_network', 'tag']
