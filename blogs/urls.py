from django.urls import path
from .views import *


app_name = 'blogs'

urlpatterns = [
    path('' , blog , name='blog_grid') ,
    path('blog-single/' , blog_detail , name='blog_single')
]
