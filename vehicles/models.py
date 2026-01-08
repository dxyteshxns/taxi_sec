from django.db import models


class Vehicle(models.Model):
    """Vehicle model for drivers"""
    
    driver = models.ForeignKey(
        'accounts.DriverProfile',
        on_delete=models.CASCADE,
        related_name='vehicles',
        verbose_name='Driver'
    )
    car_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Car Number'
    )
    car_model = models.CharField(max_length=100, verbose_name='Car Model')
    seats = models.PositiveIntegerField(default=4, verbose_name='Number of Seats')
    year = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='Year'
    )
    color = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Color'
    )
    photo = models.ImageField(
        upload_to='vehicle_photos/',
        blank=True,
        null=True,
        verbose_name='Photo'
    )
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.car_model} ({self.car_number})'
