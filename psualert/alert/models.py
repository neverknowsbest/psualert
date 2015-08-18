from django.db import models

class TimelyWarning(models.Model):
    date = models.DateTimeField()
    permanent_url = models.URLField(unique=True)
    title = models.TextField()
    description = models.TextField()
    location = models.ManyToManyField('Location')
    warning_type = models.ManyToManyField('WarningType')
    
class Location(models.Model):
    name = models.TextField()
    
class WarningType(models.Model):
    warning_type = models.TextField()
