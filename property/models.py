from django.db import models


class category_property(models.Model):
    title = models.CharField(max_length=220)
    status = models.BooleanField(default=True)


class property(models.Model):
    title = models.CharField(max_length=220)
    image = models.ImageField()
    agent = models.ForeignKey()
    category = models.ForeignKey(category_property)
    rent = models.IntegerField()
    area = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    garages = models.IntegerField()
    view = models.IntegerField()







# Create your models here.
