from django.urls import path
from .views import *


app_name = 'agents'

urlpatterns = [
    path('' , agents_grid , name='agents_grid') ,
    path('agents-grid/' , agent_single , name='agent_single')
]
