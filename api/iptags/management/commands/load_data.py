import ipaddress
import json
from django.core.management.base import BaseCommand
from iptags.models import IpTag
from django.conf import settings


class Command(BaseCommand):
    help = 'Load data into the database'

    def handle(self, *args, **options):
        data_file = settings.IP_TAG_BASE
        with open(data_file, 'r') as f:
            data = json.load(f)

            ip_tag_mapping = {}
            for item in data:
                ip_network = ipaddress.ip_network(item['ip_network'])
                tags = item['tag']
                for ip in ip_network.hosts():
                    ip_str = str(ip)
                    ip_tag_mapping.setdefault(ip_str, set()).add(tags)

            for ip, tags in ip_tag_mapping.items():
                ip_tag, created = IpTag.objects.get_or_create(ip_network=str(ip))
                ip_tag.tag = ', '.join(tags)  # Konwertujemy listę tagów na string i przypisujemy do pola tag
                ip_tag.save()  # Zapisujemy zmiany w bazie danych

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
