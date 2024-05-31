from django.urls import path

from .views import IpTagView, IpTagReportView, HomePageView, IpTagListCreateAPIView, IpTagRetrieveUpdateDestroyAPIView

app_name = 'iptags'


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ip-tags-json/<str:ip>/', IpTagView.as_view(), name='ip-tags-json'),
    path('ip-tags-report/<str:ip>/', IpTagReportView.as_view(), name='ip-tags-report'),

    path('ip-tags/', IpTagListCreateAPIView.as_view(), name='iptag-list-create'),
    path('ip-tags/<int:pk>/', IpTagRetrieveUpdateDestroyAPIView.as_view(), name='iptag-retrieve-update-destroy'),

]
