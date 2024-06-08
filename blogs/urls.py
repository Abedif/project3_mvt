from django.urls import path
from .views import *


app_name = 'blogs'

urlpatterns = [
    path('blog-single' , blogs , name='blog_single')
]
