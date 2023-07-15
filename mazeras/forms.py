from django import forms
from .models import *


class StoneForm(forms.ModelForm):
    class Meta:
        model = Stone
        fields = ['name', 'description', 'price', 'stock']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'stock': 'Stock',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    stones = forms.ModelMultipleChoiceField(queryset=Stone.objects.all(
    ), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'location',
            'stones',
            'status',
        ]

        labels = {
            'name': 'Name',
            'description': 'Description',
            'location': 'Location',
            'stones': 'Stones',
            'status': 'Completed',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class UncutMazerasForm(forms.ModelForm):
    class Meta:
        model = UncutMazeras
        fields = ['name', 'price']
        labels = {
            'name': 'Name',
            'price': 'Price',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CutMazerasForm(forms.ModelForm):
    class Meta:
        model = CutMazeras
        fields = ['name', 'price']
        labels = {
            'name': 'Name',
            'price': 'Price',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
