from django.db import models
from django.contrib.auth.models import User
from agents.models import Agents

class Category_Property(models.Model):
    title = models.CharField(max_length=220)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Property(models.Model):
    title = models.CharField(max_length=220)
    image = models.ImageField(upload_to="property" , default='default_property.jpg')
    agent = models.ForeignKey(Agents , on_delete=models.CASCADE , null=True)
    category = models.ManyToManyField(Category_Property)
    rent = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    garages = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title



# Create your models here.
