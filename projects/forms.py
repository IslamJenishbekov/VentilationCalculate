# users/forms.py
from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    """Форма для создания проекта, содержит только поле 'name'."""

    class Meta:
        model = Project
        fields = ['name']
        labels = {
            'name': 'Название проекта',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название нового проекта'})
        }
