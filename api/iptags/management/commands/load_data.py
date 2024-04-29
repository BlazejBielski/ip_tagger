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

            # Tworzymy mapowanie adresów IP do tagów na podstawie danych z bazy wiedzy
            for item in data:
                tag = item['tag']
                ip_network = ipaddress.ip_network(item['ip_network'])
                first_ip = ip_network.network_address
                last_ip = ip_network.broadcast_address

                # Dla każdego zakresu adresów IP dodajemy tagi do mapowania
                for ip in range(int(first_ip), int(last_ip) + 1):
                    ip_str = str(ipaddress.ip_address(ip))
                    if ip_str not in ip_tag_mapping:
                        ip_tag_mapping[ip_str] = set()
                    ip_tag_mapping[ip_str].add(tag)

            # Zapisujemy mapowanie do bazy danych
            for ip, tags in ip_tag_mapping.items():
                ip_tag, created = IpTag.objects.get_or_create(ip_network=str(ip))
                ip_tag.tag = ', '.join(tags)  # Konwertujemy listę tagów na string i przypisujemy do pola tag
                ip_tag.save()  # Zapisujemy zmiany w bazie danych

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
