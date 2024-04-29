from django.urls import path

from .views import IpTagView, IpTagReportView

app_name = 'iptags'

urlpatterns = [
    path('ip-tags/<str:ip>/', IpTagView.as_view(), name='ip-tags'),
    path('ip-tags-report/<str:ip>/', IpTagReportView.as_view(), name='ip-tags-report'),

]
