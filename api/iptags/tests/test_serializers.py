from iptags.serializers import IPTagSerializer


def test_serialize_no_tag():
    data = {'tag': '', 'ip_network': '192.0.2.1'}
    serializer = IPTagSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    assert serializer.data['tag'] == ''


def test_deserialize_tag():
    data = {'tag': 'Test Tag'}
    serializer = IPTagSerializer(data=data)
    assert serializer.is_valid()


# TODO
def test_deserialize_ip_network():
    pass
