from django.urls import path
from .views import *
from property.views import property_single
from agents.views import agent_single
from blogs.views import blog_detail


app_name ='root'

urlpatterns = [
    path('' , home , name='home') ,
    path('about' , about , name='about') ,
    path('contact' , contact , name = 'contact') ,
    path('prperty/<int:id>' , property_single , name = 'list_by_id') ,
    path('agent_single/<int:id>' , agent_single , name = 'list_by_agent_single') ,
    path('blog_detail/<int:id>' , blog_detail , name = 'list_by_blog_detail') ,
    
]
