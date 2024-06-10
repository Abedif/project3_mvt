from django.urls import path
from .views import *


app_name = 'blogs'

urlpatterns = [
    path('' , blog , name='blog_grid') ,
    path('blog/<str:blog>',blog ,name='list_by_blog') ,
    path('blog-single/<int:id>' , blog_detail , name='blog_single') ,
    path('blog-single/<int:id>',blog_detail,name='list_by_single_blog'),
]


