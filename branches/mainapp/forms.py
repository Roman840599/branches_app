from django import forms
from django.forms import ModelForm, TextInput, ImageField
from .models import Branch, Employee


class EmployeeForm(ModelForm):
    branch_name = forms.ModelChoiceField(queryset=Branch.objects.all())

    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'position_title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            }),
            'branch_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отделение'
            }),
        }


class BranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'

        widgets = {
            'branch_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название отделения'
            }),
            'latitude': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Широта',
                'id': 'latitude'
            }),
            'longitude': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Долгота',
                'id': 'longitude'
            }),
        }