
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_project, name="all_project"),
    
]