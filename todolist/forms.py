from django import forms
from .models import task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = [
            'title', 
            'description'
            ]