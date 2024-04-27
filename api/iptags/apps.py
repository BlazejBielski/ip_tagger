import json

from django.apps import AppConfig


class IptagsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iptags'


def ready(self):
    with open('iptags/knowledgebase/base.json', 'r') as base:
        self.base = json.load(base)