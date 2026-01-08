#!/bin/bash

# Taxi Service - Auto Setup Script for Linux
# Run this script after copying the project to Linux

echo "=========================================="
echo "  Taxi Service - Automatic Setup"
echo "=========================================="
echo ""

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
   echo "Please do not run as root. Use: bash setup.sh"
   exit 1
fi

# Update system
echo "[1/10] Updating system packages..."
sudo apt update -qq

# Install dependencies
echo "[2/10] Installing system dependencies..."
sudo apt install -y python3 python3-pip python3-venv postgresql postgresql-contrib > /dev/null 2>&1

# Start PostgreSQL
echo "[3/10] Starting PostgreSQL..."
sudo systemctl start postgresql
sudo systemctl enable postgresql > /dev/null 2>&1

# Setup database
echo "[4/10] Setting up database..."
sudo -u postgres psql << EOF > /dev/null 2>&1
DROP DATABASE IF EXISTS taxi_db_sec;
CREATE DATABASE taxi_db_sec;
DROP USER IF EXISTS node;
CREATE USER node WITH PASSWORD '9562';
GRANT ALL PRIVILEGES ON DATABASE taxi_db_sec TO node;
ALTER DATABASE taxi_db_sec OWNER TO node;
EOF

echo "     Database 'taxi_db_sec' created"
echo "     User 'node' created"

# Create virtual environment
echo "[5/10] Creating Python virtual environment..."
python3 -m venv .venv

# Activate and upgrade pip
echo "[6/10] Installing Python packages..."
source .venv/bin/activate
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1

# Run migrations
echo "[7/10] Running database migrations..."
python manage.py makemigrations > /dev/null 2>&1
python manage.py migrate > /dev/null 2>&1

# Collect static files
echo "[8/10] Collecting static files..."
python manage.py collectstatic --noinput > /dev/null 2>&1

# Load sample data
echo "[9/10] Loading sample data..."
python manage.py load_sample_data > /dev/null 2>&1

# Run tests
echo "[10/10] Running tests..."
python manage.py test > /dev/null 2>&1

echo ""
echo "=========================================="
echo "  Setup Complete!"
echo "=========================================="
echo ""
echo "Sample accounts created:"
echo "  Riders:"
echo "    - john@rider.com / password123"
echo "    - jane@rider.com / password123"
echo "  Drivers:"
echo "    - mike@driver.com / password123"
echo "    - sarah@driver.com / password123"
echo ""
echo "Next steps:"
echo "  1. Create superuser:"
echo "     source .venv/bin/activate"
echo "     python manage.py createsuperuser"
echo ""
echo "  2. Run development server:"
echo "     python manage.py runserver 0.0.0.0:8000"
echo ""
echo "  3. Open in browser:"
echo "     http://YOUR_SERVER_IP:8000"
echo ""
echo "For production deployment, see LINUX_DEPLOYMENT.md"
echo "=========================================="

