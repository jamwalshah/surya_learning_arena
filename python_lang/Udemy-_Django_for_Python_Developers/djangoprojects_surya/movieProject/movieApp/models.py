from django.db import models

# Create your models here.
class Movie(models.Model):

    name = models.CharField(max_length=40)
    releaseDate = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    # class Meta:
    #     verbose_name = _("Movie")
    #     verbose_name_plural = _("Movies")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Movie_detail", kwargs={"pk": self.pk})
