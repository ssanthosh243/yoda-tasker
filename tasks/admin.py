from django.contrib import admin
from .models import *

# Register your models here.


class APITaskAdmin(admin.ModelAdmin):
    list_display = ("callsign", "method", "url", "data", "headers")
    pass
admin.site.register(ApiTask, APITaskAdmin)
