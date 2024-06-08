
from django.urls import path
from django.contrib import admin
from .views import *


app_name = 'agents'

urlpatterns = [
    path('' , agents_grid , name='agents-grid') ,
    path('agent-single' , agent_single , name='agent-single')
]
