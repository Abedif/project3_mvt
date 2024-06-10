
from django.urls import path
from django.contrib import admin
from .views import *
from property.views import property_grid , property_single


app_name = 'agents'

urlpatterns = [
    path('' , agents_grid , name='agents-grid') ,
    path('agent-single/<int:id>' , agent_single , name='agent-single') ,
    path('property/<str:category>' , property_grid , name='list_by_category') ,
    path('detail/<int:id>' , property_single , name='list_by_id')
]
