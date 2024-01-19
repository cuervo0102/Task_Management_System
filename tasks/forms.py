from typing import Any
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta: 
        model = Task
        fields = ['processors', 'title', 'description', 'due_date', 'priority']


  
