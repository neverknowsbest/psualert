from django.db import models

class TimelyWarning(models.Model):
    date = models.DateTimeField()
    permanent_url = models.URLField()
    title = models.TextField()
    description = models.TextField()
    location = models.ManyToManyField('Location')
    warning_type = models.ManyToManyField('Warnings')
    
class Location(models.Model):
    name = models.TextField()
    
class Warning(models.Model):
    warning_name = models.TextField()
