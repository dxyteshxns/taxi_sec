# QUICK START GUIDE

## Transfer to Linux and Run

### Step 1: Copy Project to Linux

```bash
# On Linux server, extract the project
cd ~
unzip taxi_service.zip  # or use scp/sftp to upload
cd taxi_service
```

### Step 2: One-Command Setup

```bash
# Run this single command for complete setup:
sudo apt update && sudo apt install -y python3 python3-pip python3-venv postgresql postgresql-contrib && \
sudo systemctl start postgresql && \
sudo -u postgres psql -c "CREATE DATABASE taxi_db_sec;" && \
sudo -u postgres psql -c "CREATE USER node WITH PASSWORD '9562';" && \
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE taxi_db_sec TO node;" && \
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
python manage.py makemigrations && \
python manage.py migrate && \
echo "Setup complete! Now create superuser and run server."
```

### Step 3: Create Admin & Run

```bash
# Activate environment
source .venv/bin/activate

# Create admin user
python manage.py createsuperuser

# Load sample data (optional)
python manage.py load_sample_data

# Run server
python manage.py runserver 0.0.0.0:8000
```

### Step 4: Access Application

Open browser: `http://YOUR_SERVER_IP:8000`

## Default Database Credentials

Already configured in `.env` file:

- **Database**: taxi_db_sec
- **User**: node
- **Password**: 9562
- **Host**: localhost
- **Port**: 5432

## Sample Accounts (after loading sample data)

**Riders:**
- john@rider.com / password123
- jane@rider.com / password123

**Drivers:**
- mike@driver.com / password123
- sarah@driver.com / password123

## Testing

```bash
source .venv/bin/activate
python manage.py test
```

## Common Commands

```bash
# Activate environment
source .venv/bin/activate

# Run server
python manage.py runserver 0.0.0.0:8000

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data
python manage.py load_sample_data

# Run tests
python manage.py test

# Check for issues
python manage.py check
```

## Project Features

✅ User registration (Rider/Driver roles)
✅ Trip ordering and management
✅ Driver can accept/complete trips
✅ Vehicle management for drivers
✅ Driver profiles with ratings
✅ Bootstrap 5 responsive UI
✅ PostgreSQL database
✅ Admin panel
✅ Sample data loader
✅ Unit tests

## File Structure

```
taxi_service/
├── accounts/          # User auth & profiles
├── trips/            # Trip management
├── vehicles/         # Vehicle management
├── templates/        # HTML templates
├── static/           # CSS, JS
├── media/            # Uploads
├── manage.py         # Django CLI
├── requirements.txt  # Dependencies
├── .env              # Config (already set)
└── README.md         # Full docs
```

## URLs

- **Home**: http://localhost:8000/
- **Register**: http://localhost:8000/accounts/register/
- **Login**: http://localhost:8000/accounts/login/
- **Admin**: http://localhost:8000/admin/
- **Create Trip**: http://localhost:8000/trips/create/
- **My Trips**: http://localhost:8000/trips/
- **Available Trips**: http://localhost:8000/trips/available/ (drivers)
- **My Vehicles**: http://localhost:8000/vehicles/ (drivers)

## Need Help?

- Full documentation: `README.md`
- Linux deployment: `LINUX_DEPLOYMENT.md`
- Test the app: `python manage.py test`
- Check Django: `python manage.py check`

## That's It!

Your Taxi Service is ready to use! 🚕

