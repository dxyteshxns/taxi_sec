from django import forms

from .models import Vehicle


class VehicleForm(forms.ModelForm):
    """Form for creating and updating vehicles"""
    
    class Meta:
        model = Vehicle
        fields = [
            'car_number', 'car_model', 'seats',
            'year', 'color', 'photo', 'is_active'
        ]
        widgets = {
            'car_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., ABC-123'
            }),
            'car_model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Toyota Camry'
            }),
            'seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 10
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1900,
                'max': 2030
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Black'
            }),
        }
