#!/bin/bash

# Taxi Service - Quick Run Script

# Activate virtual environment
source .venv/bin/activate

# Check if database is accessible
python manage.py check --database default > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Error: Cannot connect to database."
    echo "Make sure PostgreSQL is running and database is configured."
    echo "Run: sudo systemctl start postgresql"
    exit 1
fi

# Run migrations if needed
python manage.py migrate --check > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Running pending migrations..."
    python manage.py migrate
fi

# Start development server
echo "Starting Taxi Service..."
echo "Access at: http://localhost:8000"
echo "Admin panel: http://localhost:8000/admin"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver 0.0.0.0:8000

