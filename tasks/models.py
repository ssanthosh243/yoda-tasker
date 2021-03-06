from __future__ import unicode_literals
from django.db import models
import jsonfield

# Create your models here.


class ApiTask(models.Model):
    METHOD = (
        (1, 'GET'),
        (2, 'POST')
    )

    callsign = models.CharField(max_length=100, blank=False, null=False, unique=True)
    method = models.IntegerField(choices=METHOD, default=1)
    url = models.URLField(blank=False, null=False)
    data = jsonfield.JSONField(verbose_name='Data for POST', blank=True, null=True)
    headers = jsonfield.JSONField(blank=True, null=True)

    class Meta:
        db_table = 'API Tasks'
        pass

    def __unicode__(self):
        return self.url
    pass


class Host(models.Model):
    host = models.GenericIPAddressField(blank=False, null=False)
    username = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        db_table = 'Hosts'
        pass

    def __unicode__(self):
        return self.host
    pass


class ShellTask(models.Model):
    callsign = models.CharField(max_length=100, blank=False, null=False, unique=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    command = models.CharField(max_length=1000, blank=False, null=False)

    class Meta:
        db_table = 'Shell Tasks'
        pass

    def __unicode__(self):
        return self.command
    pass
