import json

import pytest
from django.test import RequestFactory
from django.urls import reverse
from rest_framework import status
from django.http import JsonResponse

from iptags.models import IpTag
from iptags.views import IpTagView


@pytest.mark.django_db
def test_ip_tag_view_performance():
    ip_network = '192.0.2.1'
    for _ in range(1000):
        IpTag.objects.create(tag='Test Tag', ip_network=ip_network)

    factory = RequestFactory()
    request = factory.get('/ip-tags/' + ip_network)

    view = IpTagView.as_view()
    response = view(request, ip=ip_network)

    assert response.status_code == 200
    assert isinstance(response, JsonResponse)

    ip_tag_count = IpTag.objects.filter(ip_network=ip_network).count()
    response_data = json.loads(response.content)
    assert len(response_data) == ip_tag_count


@pytest.mark.django_db
def test_ip_tag_view_with_existing_ip():

    ip_tag = IpTag.objects.create(tag="Test Tag", ip_network="192.0.2.1")
    expected_url = reverse('iptags:ip-tags', kwargs={'ip': ip_tag.ip_network})
    url = reverse('iptags:ip-tags', kwargs={'ip': ip_tag.ip_network})
    response = JsonResponse([ip_tag.tag], safe=False)

    assert response.status_code == status.HTTP_200_OK
    assert url == expected_url
