from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import DriverProfile, User


class UserRegistrationForm(UserCreationForm):
    """User registration form with role selection"""
    
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.RadioSelect,
        initial='rider'
    )
    
    # Driver-specific fields (optional)
    license_number = forms.CharField(max_length=50, required=False)
    car_number = forms.CharField(max_length=20, required=False)
    car_model = forms.CharField(max_length=100, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'phone', 'role',
            'password1', 'password2'
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        
        # If driver, require driver-specific fields
        if role == 'driver':
            if not cleaned_data.get('license_number'):
                self.add_error('license_number', 'License number is required for drivers.')
            if not cleaned_data.get('car_number'):
                self.add_error('car_number', 'Car number is required for drivers.')
            if not cleaned_data.get('car_model'):
                self.add_error('car_model', 'Car model is required for drivers.')
        
        return cleaned_data


class DriverProfileForm(forms.ModelForm):
    """Form for updating driver profile"""
    
    class Meta:
        model = DriverProfile
        fields = [
            'license_number', 'description', 'car_number',
            'car_model', 'photo'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class UserUpdateForm(forms.ModelForm):
    """Form for updating user information"""
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone']
