from django.db import models
# from django.urls import reverse

# Create your models here.
class Course(models.Model):

    """Model definition for Course"""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    instructor = models.CharField(max_length=30)
    rating = models.FloatField()

    # class Meta:
    #     verbose_name = _("Course")
    #     verbose_name_plural = _("Courses")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("course_detail", kwargs={"pk": self.pk})
