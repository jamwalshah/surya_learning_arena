from django.db import models

# Create your models here.
class Course(models.Model):
    """Model definition for Course"""
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    instructor = models.CharField(max_length=20)
    rating = models.FloatField()
