from django.test import TestCase
from django.urls import reverse

from .models import DriverProfile, User


class UserModelTest(TestCase):
    def setUp(self):
        self.rider = User.objects.create_user(
            username='rider1',
            email='rider@test.com',
            password='testpass123',
            role='rider'
        )
        self.driver_user = User.objects.create_user(
            username='driver1',
            email='driver@test.com',
            password='testpass123',
            role='driver'
        )

    def test_user_creation(self):
        self.assertEqual(self.rider.email, 'rider@test.com')
        self.assertEqual(self.rider.role, 'rider')
        self.assertTrue(self.rider.is_rider())
        self.assertFalse(self.rider.is_driver())

    def test_driver_role(self):
        self.assertEqual(self.driver_user.role, 'driver')
        self.assertTrue(self.driver_user.is_driver())
        self.assertFalse(self.driver_user.is_rider())


class DriverProfileModelTest(TestCase):
    def setUp(self):
        self.driver_user = User.objects.create_user(
            username='driver1',
            email='driver@test.com',
            password='testpass123',
            role='driver'
        )
        self.driver_profile = DriverProfile.objects.create(
            user=self.driver_user,
            license_number='DL123456',
            car_number='ABC-123',
            car_model='Toyota Camry'
        )

    def test_driver_profile_creation(self):
        self.assertEqual(self.driver_profile.license_number, 'DL123456')
        self.assertEqual(self.driver_profile.car_model, 'Toyota Camry')
        self.assertEqual(self.driver_profile.rating, 5.00)

    def test_driver_profile_str(self):
        expected = f'{self.driver_user.email} - Toyota Camry'
        self.assertEqual(str(self.driver_profile), expected)


class RegistrationViewTest(TestCase):
    def test_registration_view_get(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_rider_registration(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'newrider',
            'email': 'newrider@test.com',
            'password1': 'testpass123!',
            'password2': 'testpass123!',
            'role': 'rider',
        })
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.role, 'rider')
