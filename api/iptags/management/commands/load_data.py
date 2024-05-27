import ipaddress
import json
from django.core.management.base import BaseCommand
from iptags.models import IpTag
from django.conf import settings
from django.db import transaction


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

        # Fetch existing IpTags
        existing_ip_tags = IpTag.objects.all()
        existing_ip_dict = {ip_tag.ip_network: ip_tag for ip_tag in existing_ip_tags}

        new_ip_tags = []
        with transaction.atomic():
            for ip, tags in ip_tag_mapping.items():
                if ip in existing_ip_dict:
                    ip_tag = existing_ip_dict[ip]
                    ip_tag.tag = ', '.join(tags)
                    ip_tag.save()  # Save if updating existing record
                else:
                    new_ip_tags.append(IpTag(ip_network=str(ip), tag=', '.join(tags)))

            # Bulk create new IpTags
            if new_ip_tags:
                IpTag.objects.bulk_create(new_ip_tags, batch_size=1000)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
