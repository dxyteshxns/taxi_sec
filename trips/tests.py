from django.test import TestCase
from django.urls import reverse

from accounts.models import DriverProfile, User

from .models import Trip


class TripModelTest(TestCase):
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
        self.driver_profile = DriverProfile.objects.create(
            user=self.driver_user,
            license_number='DL123456',
            car_number='ABC-123',
            car_model='Toyota Camry'
        )

    def test_trip_creation(self):
        trip = Trip.objects.create(
            rider=self.rider,
            origin='123 Main St',
            destination='456 Oak Ave',
            status='requested'
        )
        self.assertEqual(trip.origin, '123 Main St')
        self.assertEqual(trip.status, 'requested')
        self.assertIsNone(trip.driver)

    def test_trip_can_be_edited(self):
        trip = Trip.objects.create(
            rider=self.rider,
            origin='123 Main St',
            destination='456 Oak Ave',
            status='requested'
        )
        self.assertTrue(trip.can_be_edited())
        
        trip.status = 'accepted'
        trip.save()
        self.assertFalse(trip.can_be_edited())

    def test_trip_accept(self):
        trip = Trip.objects.create(
            rider=self.rider,
            origin='123 Main St',
            destination='456 Oak Ave',
            status='requested'
        )
        self.assertTrue(trip.can_be_accepted())
        
        trip.driver = self.driver_profile
        trip.status = 'accepted'
        trip.save()
        
        self.assertFalse(trip.can_be_accepted())
        self.assertEqual(trip.driver, self.driver_profile)


class TripViewsTest(TestCase):
    def setUp(self):
        self.rider = User.objects.create_user(
            username='rider1',
            email='rider@test.com',
            password='testpass123',
            role='rider'
        )
        self.client.login(username='rider@test.com', password='testpass123')

    def test_trip_create_view(self):
        response = self.client.get(reverse('trips:trip_create'))
        self.assertEqual(response.status_code, 200)

    def test_create_trip(self):
        response = self.client.post(reverse('trips:trip_create'), {
            'origin': '123 Main St',
            'destination': '456 Oak Ave',
            'comment': 'Please hurry'
        })
        self.assertEqual(Trip.objects.count(), 1)
        trip = Trip.objects.first()
        self.assertEqual(trip.origin, '123 Main St')
        self.assertEqual(trip.rider, self.rider)
