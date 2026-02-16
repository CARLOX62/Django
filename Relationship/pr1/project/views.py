from django.shortcuts import render
from .models import projectVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_project(request):
    projects = projectVarity.objects.all()
    return render(request, 'app/all_index.html', {'projects': projects})

def project_details(request, project_id):
    pr1 = get_object_or_404(projectVarity, pk=project_id)
    return render(request, 'app/project_details.html', {'pr1': pr1})