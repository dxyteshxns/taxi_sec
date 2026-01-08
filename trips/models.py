from django.conf import settings
from django.db import models


class Trip(models.Model):
    """Trip model for ride requests"""
    
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    rider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='trips',
        verbose_name='Rider'
    )
    driver = models.ForeignKey(
        'accounts.DriverProfile',
        on_delete=models.SET_NULL,
        related_name='driver_trips',
        null=True,
        blank=True,
        verbose_name='Driver'
    )
    origin = models.CharField(max_length=255, verbose_name='Origin')
    destination = models.CharField(max_length=255, verbose_name='Destination')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='requested',
        verbose_name='Status'
    )
    comment = models.TextField(blank=True, verbose_name='Comment')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Price'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    
    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Trip #{self.id}: {self.origin} -> {self.destination}'
    
    def can_be_edited(self):
        """Check if trip can be edited by rider"""
        return self.status == 'requested'
    
    def can_be_accepted(self):
        """Check if trip can be accepted by driver"""
        return self.status == 'requested'
    
    def can_be_completed(self):
        """Check if trip can be completed"""
        return self.status == 'accepted'
    
    def can_be_cancelled(self):
        """Check if trip can be cancelled"""
        return self.status in ['requested', 'accepted']
