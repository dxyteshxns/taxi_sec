from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import VehicleForm
from .models import Vehicle


class VehicleListView(LoginRequiredMixin, ListView):
    """List all vehicles for the current driver"""
    model = Vehicle
    template_name = 'vehicles/vehicle_list.html'
    context_object_name = 'vehicles'
    paginate_by = 10
    
    def get_queryset(self):
        if self.request.user.is_driver():
            return Vehicle.objects.filter(driver=self.request.user.driver_profile)
        return Vehicle.objects.none()


class VehicleDetailView(LoginRequiredMixin, DetailView):
    """Detail view for a vehicle"""
    model = Vehicle
    template_name = 'vehicles/vehicle_detail.html'
    context_object_name = 'vehicle'


class VehicleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Create a new vehicle"""
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicles:vehicle_list')
    
    def test_func(self):
        return self.request.user.is_driver()
    
    def form_valid(self, form):
        form.instance.driver = self.request.user.driver_profile
        messages.success(self.request, 'Vehicle created successfully!')
        return super().form_valid(form)


class VehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update an existing vehicle"""
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicles/vehicle_form.html'
    success_url = reverse_lazy('vehicles:vehicle_list')
    
    def test_func(self):
        vehicle = self.get_object()
        return (
            self.request.user.is_driver() and
            vehicle.driver == self.request.user.driver_profile
        )
    
    def form_valid(self, form):
        messages.success(self.request, 'Vehicle updated successfully!')
        return super().form_valid(form)


class VehicleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a vehicle"""
    model = Vehicle
    template_name = 'vehicles/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicles:vehicle_list')
    
    def test_func(self):
        vehicle = self.get_object()
        return (
            self.request.user.is_driver() and
            vehicle.driver == self.request.user.driver_profile
        )
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Vehicle deleted successfully!')
        return super().delete(request, *args, **kwargs)
