# Taxi Service - Django Web Application

A full-featured taxi service web application built with Django and PostgreSQL. This application allows passengers to order rides and drivers to accept and manage trips.

## Features

### For Passengers (Riders)
- Register and create an account
- Order taxi rides with pickup and destination
- View trip history
- Track trip status (Requested, Accepted, Completed, Cancelled)
- View driver information and vehicle details
- Edit or cancel trips before they are accepted

### For Drivers
- Register as a driver with license and vehicle information
- View available trip requests
- Accept trip requests
- Manage personal vehicles
- Complete or cancel trips
- Maintain driver profile with rating

### Admin Features
- Full CRUD operations for all models
- User management
- Trip monitoring and management
- Driver and vehicle verification

## Technology Stack

- **Backend**: Django 4.2+
- **Database**: PostgreSQL
- **Frontend**: Bootstrap 5, HTML, CSS, JavaScript
- **Authentication**: Django built-in authentication
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Code Quality**: Black, Flake8, isort, pre-commit

## Requirements

- Python 3.10+
- PostgreSQL 12+
- pip (Python package manager)

## Installation

### 1. Clone or Extract the Project

```bash
cd taxi_service
```

### 2. Create Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL Database

Make sure PostgreSQL is installed and running. Create the database:

```bash
sudo -u postgres psql
CREATE DATABASE taxi_db_sec;
CREATE USER node WITH PASSWORD '9562';
GRANT ALL PRIVILEGES ON DATABASE taxi_db_sec TO node;
\q
```

### 5. Configure Environment Variables

The `.env` file already contains the required PostgreSQL settings:

```ini
DJANGO_SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

POSTGRES_DB_NAME=taxi_db_sec
POSTGRES_USER=node
POSTGRES_PASSWORD=9562
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

**Important**: In production, change the `DJANGO_SECRET_KEY` and set `DEBUG=False`.

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 8. Load Sample Data (Optional)

```bash
python manage.py load_sample_data
```

This will create:
- 2 riders (john@rider.com, jane@rider.com)
- 2 drivers (mike@driver.com, sarah@driver.com)
- 2 vehicles
- 5 sample trips

All sample accounts use the password: `password123`

### 9. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Project Structure

```
taxi_service/
├── accounts/               # User authentication and profiles
├── trips/                 # Trip management
├── vehicles/              # Vehicle management
├── taxi_project/          # Main project settings
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS)
├── media/                 # User-uploaded files
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Usage

### For Passengers

1. **Register**: Go to `/accounts/register/` and create an account with role "Rider"
2. **Order Taxi**: Click "Order a Taxi" or visit `/trips/create/`
3. **Enter Details**: Fill in pickup location, destination, and optional comments
4. **Track Trip**: View your trips at `/trips/`
5. **View Driver**: Once accepted, see driver information on the trip detail page

### For Drivers

1. **Register**: Go to `/accounts/register/` and create an account with role "Driver"
   - Provide license number, car details during registration
2. **View Available Trips**: Visit `/trips/available/`
3. **Accept Trip**: Click "Accept Trip" on any available request
4. **Complete Trip**: Mark the trip as completed when finished
5. **Manage Vehicles**: Add/edit vehicles at `/vehicles/`

### Admin Panel

Access the admin panel at `/admin/` using superuser credentials.

## Testing

Run the test suite:

```bash
python manage.py test
```

Run specific app tests:

```bash
python manage.py test accounts
python manage.py test trips
python manage.py test vehicles
```

## Code Quality

### Format Code

```bash
black .
isort .
```

### Check Code Quality

```bash
flake8
```

## Database Schema

### User Model
- email (unique, used for authentication)
- username
- phone
- role (rider/driver)

### DriverProfile Model
- user (OneToOne with User)
- license_number (unique)
- car_number, car_model
- photo, rating

### Vehicle Model
- driver (ForeignKey to DriverProfile)
- car_number (unique)
- car_model, seats, year, color

### Trip Model
- rider, driver (optional)
- origin, destination
- status (requested/accepted/completed/cancelled)
- comment, price

## Troubleshooting

### Database Connection Error

1. Make sure PostgreSQL is running
2. Verify database exists
3. Check `.env` credentials
4. Ensure user has proper permissions

### Migration Issues

```bash
python manage.py makemigrations
python manage.py migrate
```

## Production Deployment (Linux)

```bash
# Install dependencies
sudo apt update
sudo apt install python3-pip python3-venv postgresql nginx

# Setup PostgreSQL
sudo -u postgres psql
CREATE DATABASE taxi_db_sec;
CREATE USER node WITH PASSWORD '9562';
GRANT ALL PRIVILEGES ON DATABASE taxi_db_sec TO node;
\q

# Setup project
cd /path/to/taxi_service
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run migrations
python manage.py migrate
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser

# Load sample data (optional)
python manage.py load_sample_data

# Run server
python manage.py runserver 0.0.0.0:8000
```

## Important Security Notes

1. Change `DJANGO_SECRET_KEY` in production
2. Set `DEBUG=False` in production
3. Update `ALLOWED_HOSTS` with your domain
4. Use HTTPS in production
5. Setup firewall rules
6. Regular database backups

## API Endpoints

### Authentication
- `POST /accounts/register/` - Register new user
- `POST /accounts/login/` - Login
- `POST /accounts/logout/` - Logout
- `GET /accounts/profile/` - View profile

### Trips
- `GET /trips/` - List trips
- `POST /trips/create/` - Create trip
- `GET /trips/<id>/` - Trip details
- `POST /trips/<id>/accept/` - Accept trip (drivers)
- `POST /trips/<id>/complete/` - Complete trip
- `POST /trips/<id>/cancel/` - Cancel trip

### Vehicles
- `GET /vehicles/` - List vehicles
- `POST /vehicles/create/` - Create vehicle
- `GET /vehicles/<id>/` - Vehicle details

## Support

For issues:
- Django docs: https://docs.djangoproject.com/
- PostgreSQL docs: https://www.postgresql.org/docs/

## License

Educational purposes.

---

**Ready to deploy on Linux with PostgreSQL!**

