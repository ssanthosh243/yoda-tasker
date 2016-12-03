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
