from django.db import models


class IpTag(models.Model):
    tag = models.CharField(max_length=16)
    ip_network = models.GenericIPAddressField(unpack_ipv4=True)
