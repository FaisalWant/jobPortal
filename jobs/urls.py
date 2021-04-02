from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name= "jobs"
urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),
    path('/create-job/', CreateJobView.as_view(), name='create-job'),
    path('search/', SearchJobView.as_view(), name='search'),
    path('detail/<slug>/<int:pk>/', SingleJobView.as_view(), name='single-job'),
    path('category-detail/<slug>/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

]