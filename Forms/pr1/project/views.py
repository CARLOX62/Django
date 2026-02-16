from django.shortcuts import render
from .models import projectVarity, Store
from django.shortcuts import get_object_or_404
from .forms import projectVarityForm

# Create your views here.
def all_project(request):
    projects = projectVarity.objects.all()
    return render(request, 'app/all_index.html', {'projects': projects})

def project_details(request, project_id):
    pr1 = get_object_or_404(projectVarity, pk=project_id)
    return render(request, 'app/project_details.html', {'pr1': pr1})


def project_store_view(request):
    stores = None
    if request.method == 'POST':
        form = projectVarityForm(request.POST)
        if form.is_valid():
            project_varity = form.cleaned_data['project_varity']
            Store.objects.filter(project_varieties= project_varity)
    else:
        form = projectVarityForm()

    return render(request, 'app/project_store.html', {'stores': stores, 'form': form})