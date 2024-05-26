from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from iptags.models import IpTag

User = get_user_model()


# class UserAdminConfig(UserAdmin):
#     list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
#     list_filter = ('is_staff', 'is_active', 'date_joined')
#     ordering = ('-last_login',)
#     search_fields = ('email', 'username')


class IpTagAdminConfig(admin.ModelAdmin):
    list_display = ('ip_network', 'tag')
    list_filter = ('ip_network', 'tag')
    ordering = ('ip_network',)
    search_fields = ('ip_network', 'tag')


admin.site.register(IpTag, IpTagAdminConfig)
# admin.site.register(User, UserAdminConfig)
