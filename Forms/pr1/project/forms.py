from django import forms
from .models import projectVarity

class projectVarityForm(forms.Form):
    project_varity =forms.ModelChoiceField(queryset=projectVarity.objects.all(), label='Select Project Variety')