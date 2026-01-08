from django import forms

from .models import Trip


class TripCreateForm(forms.ModelForm):
    """Form for creating a new trip"""
    
    class Meta:
        model = Trip
        fields = ['origin', 'destination', 'comment']
        widgets = {
            'origin': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter pickup location'
            }),
            'destination': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter destination'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Additional comments (optional)'
            }),
        }


class TripUpdateForm(forms.ModelForm):
    """Form for updating trip information"""
    
    class Meta:
        model = Trip
        fields = ['origin', 'destination', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
