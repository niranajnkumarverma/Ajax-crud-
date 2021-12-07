from django import urls
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('add_new/', add_new, name='add_new'),
    path('update_data/<int:pk>/', update_data, name='update_data'),
    path('delete_data/<int:pk>/', delete_data, name='delete_data'),
]