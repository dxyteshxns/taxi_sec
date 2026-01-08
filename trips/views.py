from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import TripCreateForm, TripUpdateForm
from .models import Trip


class TripListView(LoginRequiredMixin, ListView):
    """List all trips for the current user"""
    model = Trip
    template_name = 'trips/trip_list.html'
    context_object_name = 'trips'
    paginate_by = 10
    
    def get_queryset(self):
        user = self.request.user
        if user.is_driver():
            return Trip.objects.filter(driver=user.driver_profile)
        return Trip.objects.filter(rider=user)


class TripDetailView(LoginRequiredMixin, DetailView):
    """Detail view for a trip"""
    model = Trip
    template_name = 'trips/trip_detail.html'
    context_object_name = 'trip'


class TripCreateView(LoginRequiredMixin, CreateView):
    """Create a new trip"""
    model = Trip
    form_class = TripCreateForm
    template_name = 'trips/trip_create.html'
    success_url = reverse_lazy('trips:trip_list')
    
    def form_valid(self, form):
        form.instance.rider = self.request.user
        messages.success(self.request, 'Trip created successfully!')
        return super().form_valid(form)


class TripUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update an existing trip"""
    model = Trip
    form_class = TripUpdateForm
    template_name = 'trips/trip_update.html'
    success_url = reverse_lazy('trips:trip_list')
    
    def test_func(self):
        trip = self.get_object()
        return trip.rider == self.request.user and trip.can_be_edited()
    
    def form_valid(self, form):
        messages.success(self.request, 'Trip updated successfully!')
        return super().form_valid(form)


class TripDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a trip"""
    model = Trip
    template_name = 'trips/trip_confirm_delete.html'
    success_url = reverse_lazy('trips:trip_list')
    
    def test_func(self):
        trip = self.get_object()
        return trip.rider == self.request.user and trip.can_be_edited()
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Trip deleted successfully!')
        return super().delete(request, *args, **kwargs)


class AvailableTripsView(LoginRequiredMixin, ListView):
    """List available trips for drivers"""
    model = Trip
    template_name = 'trips/available_trips.html'
    context_object_name = 'trips'
    paginate_by = 10
    
    def get_queryset(self):
        return Trip.objects.filter(status='requested')


@login_required
def accept_trip(request, pk):
    """Accept a trip as a driver"""
    if not request.user.is_driver():
        messages.error(request, 'Only drivers can accept trips.')
        return redirect('trips:trip_list')
    
    trip = get_object_or_404(Trip, pk=pk)
    
    if not trip.can_be_accepted():
        messages.error(request, 'This trip cannot be accepted.')
        return redirect('trips:available_trips')
    
    trip.driver = request.user.driver_profile
    trip.status = 'accepted'
    trip.save()
    
    messages.success(request, 'Trip accepted successfully!')
    return redirect('trips:trip_detail', pk=trip.pk)


@login_required
def complete_trip(request, pk):
    """Complete a trip"""
    trip = get_object_or_404(Trip, pk=pk)
    
    if not request.user.is_driver() or trip.driver != request.user.driver_profile:
        messages.error(request, 'You do not have permission to complete this trip.')
        return redirect('trips:trip_list')
    
    if not trip.can_be_completed():
        messages.error(request, 'This trip cannot be completed.')
        return redirect('trips:trip_detail', pk=trip.pk)
    
    trip.status = 'completed'
    trip.save()
    
    messages.success(request, 'Trip completed successfully!')
    return redirect('trips:trip_detail', pk=trip.pk)


@login_required
def cancel_trip(request, pk):
    """Cancel a trip"""
    trip = get_object_or_404(Trip, pk=pk)
    
    # Check permissions
    is_rider = trip.rider == request.user
    is_driver = request.user.is_driver() and trip.driver == request.user.driver_profile
    
    if not (is_rider or is_driver):
        messages.error(request, 'You do not have permission to cancel this trip.')
        return redirect('trips:trip_list')
    
    if not trip.can_be_cancelled():
        messages.error(request, 'This trip cannot be cancelled.')
        return redirect('trips:trip_detail', pk=trip.pk)
    
    trip.status = 'cancelled'
    trip.save()
    
    messages.success(request, 'Trip cancelled successfully!')
    return redirect('trips:trip_detail', pk=trip.pk)
