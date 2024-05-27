from django.urls import path

from .views import IpTagView, IpTagReportView, IPTagListView, IPTagCreateView, IPTagUpdateView, IPTagDeleteView, \
    IPTagRetrieveAPIView

app_name = 'iptags'


urlpatterns = [
    path('ip-tags/<str:ip>/', IpTagView.as_view(), name='ip-tags'),
    path('ip-tags-report/<str:ip>/', IpTagReportView.as_view(), name='ip-tags-report'),
    path('ip-tags/', IPTagListView.as_view(), name='ip-tags-list'),
    path('ip-tags/', IPTagCreateView.as_view(), name='ip-tags-create'),
    path('ip-tags/<int:id>/', IPTagUpdateView.as_view(), name='ip-tags-update'),
    path('ip-tags/<int:id>/', IPTagDeleteView.as_view(), name='ip-tags-delete'),
    path('ip-tags/<int:id>/', IPTagRetrieveAPIView.as_view(), name='ip-tags-retrieve'),

]
