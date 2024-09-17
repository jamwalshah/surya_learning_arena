from django.db import models

# Create your models here.
class Student(models.Model):
    """Model definition for Student."""
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    testScore = models.FloatField()

    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        """Unicode representation of Student."""
        pass
