from django.urls import path

from .views import IPTagsListView

app_name = 'iptags'

urlpatterns = [
    path('ip-tags/{ip}', IPTagsListView.as_view(), name='ip-tags-list'),

]
