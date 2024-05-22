from django.db import models


class IpTag(models.Model):
    """Model for representing IP matched with tags.

    :param tag: tag for IP address
    :type tag: str
    :param ip_network: IP address
    :type ip_network: str
    """
    tag = models.CharField(max_length=16)
    ip_network = models.GenericIPAddressField(unpack_ipv4=True)

    def __str__(self):
        return self.tag
