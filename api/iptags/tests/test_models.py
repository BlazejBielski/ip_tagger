import time

import pytest

from django.db import DataError

from iptags.models import IpTag


@pytest.mark.django_db
def test_create_iptag():
    iptag = IpTag.objects.create(tag="Test Tag", ip_network="192.0.2.1")
    assert iptag.tag == "Test Tag"
    assert iptag.ip_network == "192.0.2.1"


@pytest.mark.django_db
def test_performance():
    start_time = time.time()
    for _ in range(1000):
        IpTag.objects.create(tag="Test Tag", ip_network="192.0.2.1")
    creation_time = time.time() - start_time
    assert creation_time < 1.0


@pytest.mark.django_db()
def test_invalid_ip_address():
    with pytest.raises(DataError):
        IpTag.objects.create(tag="Test Tag", ip_network="10.0.0.354")


@pytest.mark.django_db
def test_invalid_tag():
    with pytest.raises(DataError):
        IpTag.objects.create(tag="Test Tag" * 5, ip_network="192.0.2.1")


# TODO
@pytest.mark.django_db
def test_valid_ip_address():
    pass


# TODO
@pytest.mark.django_db
def test_valid_tag():
    pass
