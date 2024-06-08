from django.urls import path
from .views import *


app_name ='root'

urlpatterns = [
    path('' , home , name='home') ,
    path('about' , about , name='about') ,
    path('contact' , contact , name = 'contact') ,
    path('blog-grid' , blogs , name='blogs') ,
    path('property-grid' , property_grid , name='property') ,
    path('/agents_grid' , agents_grid , name='agents_grid')
]
