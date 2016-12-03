from django.contrib import admin
from .models import *

# Register your models here.


class APITaskAdmin(admin.ModelAdmin):
    list_display = ("callsign", "method", "url", "data", "headers")
    pass
admin.site.register(ApiTask, APITaskAdmin)


class HostsAdmin(admin.ModelAdmin):
    list_display = ("host", "username", "password")
    pass
admin.site.register(Host, HostsAdmin)


class ShellTasksAdmin(admin.ModelAdmin):
    list_display = ("callsign", "host", "command")
    pass
admin.site.register(ShellTask, ShellTasksAdmin)
