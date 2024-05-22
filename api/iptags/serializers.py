from rest_framework import serializers

from .models import IpTag


class IPTagSerializer(serializers.ModelSerializer):
    """Serializer for IpTag model.

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
