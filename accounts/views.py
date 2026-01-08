from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import DriverProfileForm, UserRegistrationForm, UserUpdateForm
from .models import DriverProfile


class CustomLoginView(LoginView):
    """Custom login view"""
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    """Custom logout view"""
    next_page = reverse_lazy('home')


def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = form.save(commit=False)
                user.role = form.cleaned_data['role']
                user.save()
                
                # If driver, create driver profile
                if user.role == 'driver':
                    DriverProfile.objects.create(
                        user=user,
                        license_number=form.cleaned_data['license_number'],
                        car_number=form.cleaned_data['car_number'],
                        car_model=form.cleaned_data['car_model'],
                        description=form.cleaned_data.get('description', '')
                    )
                
                login(request, user)
                messages.success(request, 'Registration successful!')
                return redirect('home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    """User profile view"""
    return render(request, 'accounts/profile.html')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Update user profile"""
    model = DriverProfile
    form_class = DriverProfileForm
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('accounts:profile')
    
    def get_object(self, queryset=None):
        return self.request.user.driver_profile
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)


@login_required
def update_user_info(request):
    """Update user basic information"""
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Information updated successfully!')
            return redirect('accounts:profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'accounts/update_info.html', {'form': form})
