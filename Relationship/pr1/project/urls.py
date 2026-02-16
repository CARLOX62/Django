
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_project, name="all_project"),
    path('<int:project_id>/', views.project_details, name="project_details"),
    
]