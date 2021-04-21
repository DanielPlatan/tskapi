from django.db import models

class Metrics(models.Model):
    date = models.DateField(null=True)
    channel = models.CharField(max_length=150, null=True)
    country = models.CharField(max_length=150, null=True)
    os = models.CharField(max_length=150, null=True)
    impressions = models.IntegerField(null=True)
    clicks = models.IntegerField(null=True)
    installs = models.IntegerField(null=True)
    spend = models.FloatField(null=True)
    revenue = models.FloatField(null=True)

    def cpi(self):
        return None