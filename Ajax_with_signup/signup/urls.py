from django.contrib import admin
from django.urls import path
from .views import index ,signup,validate_email

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('ajax/validate_email',validate_email, name='validate_email'),
]
