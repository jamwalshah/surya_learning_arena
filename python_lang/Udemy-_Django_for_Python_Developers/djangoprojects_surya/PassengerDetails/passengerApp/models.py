from django.db import models

# Create your models here.
class PassengerPatal(models.Model):
  firstName = models.CharField(max_length=30)
  lastName = models.CharField(max_length=30)
  email = models.EmailField(max_length=35)
  rewardPoints = models.PositiveIntegerField()
  