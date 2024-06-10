from django.db import models
from django.contrib.auth.models import User

class Agents(models.Model):
    title = models.CharField(max_length=220)
    image = models.ImageField(upload_to='agent' , default='default_property.jpg')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    description = models.TextField()
    phone = models.CharField(max_length=110 , default=0)
    email = models.EmailField(null=True)
    facebook = models.CharField(max_length=300 , default='#')
    x = models.CharField(max_length=300 , default='#')
    instagram = models.CharField(max_length=300 , default='#')
    linkedin = models.CharField(max_length=300 , default='#')
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title




# Create your models here.
