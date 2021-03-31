from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name= "jobs"
urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),
]