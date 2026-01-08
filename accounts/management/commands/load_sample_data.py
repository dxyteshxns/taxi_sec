from django.core.management.base import BaseCommand
from django.db import transaction

from accounts.models import DriverProfile, User
from trips.models import Trip
from vehicles.models import Vehicle


class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Loading sample data...')
        
        with transaction.atomic():
            # Create riders
            rider1 = User.objects.create_user(
                username='john_rider',
                email='john@rider.com',
                password='password123',
                phone='+1234567890',
                role='rider',
                first_name='John',
                last_name='Doe'
            )
            
            rider2 = User.objects.create_user(
                username='jane_rider',
                email='jane@rider.com',
                password='password123',
                phone='+1234567891',
                role='rider',
                first_name='Jane',
                last_name='Smith'
            )
            
            # Create drivers
            driver1_user = User.objects.create_user(
                username='mike_driver',
                email='mike@driver.com',
                password='password123',
                phone='+1234567892',
                role='driver',
                first_name='Mike',
                last_name='Johnson'
            )
            
            driver1_profile = DriverProfile.objects.create(
                user=driver1_user,
                license_number='DL001234',
                car_number='ABC-123',
                car_model='Toyota Camry 2020',
                description='Friendly and professional driver with 5 years of experience.',
                rating=4.85
            )
            
            driver2_user = User.objects.create_user(
                username='sarah_driver',
                email='sarah@driver.com',
                password='password123',
                phone='+1234567893',
                role='driver',
                first_name='Sarah',
                last_name='Williams'
            )
            
            driver2_profile = DriverProfile.objects.create(
                user=driver2_user,
                license_number='DL005678',
                car_number='XYZ-789',
                car_model='Honda Accord 2021',
                description='Safe driver with excellent customer service.',
                rating=4.92
            )
            
            # Create vehicles
            Vehicle.objects.create(
                driver=driver1_profile,
                car_number='ABC-123',
                car_model='Toyota Camry 2020',
                seats=4,
                year=2020,
                color='Silver',
                is_active=True
            )
            
            Vehicle.objects.create(
                driver=driver2_profile,
                car_number='XYZ-789',
                car_model='Honda Accord 2021',
                seats=4,
                year=2021,
                color='Black',
                is_active=True
            )
            
            # Create trips
            Trip.objects.create(
                rider=rider1,
                driver=driver1_profile,
                origin='123 Main Street, Downtown',
                destination='456 Oak Avenue, Uptown',
                status='completed',
                comment='Please take the highway',
                price=25.50
            )
            
            Trip.objects.create(
                rider=rider1,
                driver=driver2_profile,
                origin='789 Pine Road, Suburb',
                destination='321 Elm Street, City Center',
                status='completed',
                comment='',
                price=18.75
            )
            
            Trip.objects.create(
                rider=rider2,
                driver=driver1_profile,
                origin='555 Maple Drive, North Side',
                destination='888 Cedar Lane, South Side',
                status='accepted',
                comment='Arriving in 10 minutes'
            )
            
            Trip.objects.create(
                rider=rider1,
                origin='100 Park Avenue, East End',
                destination='200 Lake Road, West End',
                status='requested',
                comment='Need a ride ASAP'
            )
            
            Trip.objects.create(
                rider=rider2,
                origin='777 Beach Boulevard',
                destination='999 Mountain View',
                status='requested',
                comment=''
            )
            
        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data!'))
        self.stdout.write('\nCreated users:')
        self.stdout.write('  Riders:')
        self.stdout.write('    - john@rider.com (password: password123)')
        self.stdout.write('    - jane@rider.com (password: password123)')
        self.stdout.write('  Drivers:')
        self.stdout.write('    - mike@driver.com (password: password123)')
        self.stdout.write('    - sarah@driver.com (password: password123)')
