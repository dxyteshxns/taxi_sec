from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model with email as username field"""
    
    ROLE_CHOICES = [
        ('rider', 'Rider'),
        ('driver', 'Driver'),
    ]
    
    email = models.EmailField(unique=True, verbose_name='Email Address')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Phone Number')
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='rider',
        verbose_name='Role'
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.email
    
    def is_driver(self):
        return self.role == 'driver'
    
    def is_rider(self):
        return self.role == 'rider'


class DriverProfile(models.Model):
    """Driver profile with additional information"""
    
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        related_name='driver_profile',
        verbose_name='User'
    )
    license_number = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='License Number'
    )
    description = models.TextField(blank=True, verbose_name='Description')
    car_number = models.CharField(max_length=20, verbose_name='Car Number')
    car_model = models.CharField(max_length=100, verbose_name='Car Model')
    photo = models.ImageField(
        upload_to='driver_photos/',
        blank=True,
        null=True,
        verbose_name='Photo'
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=5.00,
        verbose_name='Rating'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Driver Profile'
        verbose_name_plural = 'Driver Profiles'
    
    def __str__(self):
        return f'{self.user.email} - {self.car_model}'
