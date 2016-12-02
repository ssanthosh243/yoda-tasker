from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ApiTask(models.Model):
    METHOD = (
        (1, 'GET'),
        (2, 'POST')
    )

    callsign = models.CharField(max_length=100, blank=False, null=False)
    method = models.IntegerField(choices=METHOD, default=1)
    url = models.URLField(blank=False, null=False)
    data = models.CharField(verbose_name='Data for POST', max_length=1000, blank=True, null=True)
    headers = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'API Tasks'
        pass

    def __unicode__(self):
        return self.url
    pass
