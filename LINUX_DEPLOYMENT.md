# Linux Deployment Guide

## Quick Start on Linux

### 1. Upload Project to Linux Server

```bash
# Extract or clone the project
cd /home/your_username
# Assuming you uploaded taxi_service.zip
unzip taxi_service.zip
cd taxi_service
```

### 2. Install System Dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv postgresql postgresql-contrib
```

### 3. Setup PostgreSQL

```bash
# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database and user
sudo -u postgres psql << EOF
CREATE DATABASE taxi_db_sec;
CREATE USER node WITH PASSWORD '9562';
GRANT ALL PRIVILEGES ON DATABASE taxi_db_sec TO node;
ALTER DATABASE taxi_db_sec OWNER TO node;
\q
EOF
```

### 4. Setup Python Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### 5. Run Migrations

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Load Sample Data (Optional)

```bash
python manage.py load_sample_data
```

### 8. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 9. Test Run

```bash
# Run development server
python manage.py runserver 0.0.0.0:8000
```

Visit `http://your_server_ip:8000` in browser.

### 10. Run Tests

```bash
python manage.py test
```

## Production Setup with Gunicorn & Nginx

### Install Gunicorn

```bash
pip install gunicorn
```

### Create Gunicorn Service

```bash
sudo nano /etc/systemd/system/taxi_service.service
```

Add:

```ini
[Unit]
Description=Taxi Service Django App
After=network.target

[Service]
User=your_username
Group=www-data
WorkingDirectory=/home/your_username/taxi_service
Environment="PATH=/home/your_username/taxi_service/.venv/bin"
ExecStart=/home/your_username/taxi_service/.venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/home/your_username/taxi_service/taxi_service.sock \
          taxi_project.wsgi:application

[Install]
WantedBy=multi-user.target
```

### Start Service

```bash
sudo systemctl start taxi_service
sudo systemctl enable taxi_service
sudo systemctl status taxi_service
```

### Configure Nginx

```bash
sudo nano /etc/nginx/sites-available/taxi_service
```

Add:

```nginx
server {
    listen 80;
    server_name your_domain_or_ip;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/your_username/taxi_service;
    }
    
    location /media/ {
        root /home/your_username/taxi_service;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/your_username/taxi_service/taxi_service.sock;
    }
}
```

### Enable Nginx Site

```bash
sudo ln -s /etc/nginx/sites-available/taxi_service /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### Set Permissions

```bash
chmod 755 /home/your_username
chmod 755 /home/your_username/taxi_service
sudo chown -R your_username:www-data /home/your_username/taxi_service
```

## Firewall Configuration

```bash
# Allow SSH, HTTP, HTTPS
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

## Environment Variables for Production

Edit `.env`:

```bash
nano .env
```

Update:

```ini
DEBUG=False
ALLOWED_HOSTS=your_domain.com,your_ip_address
DJANGO_SECRET_KEY=generate_new_secret_key_here
```

## Database Backup

```bash
# Backup
pg_dump -U node taxi_db_sec > backup_$(date +%Y%m%d).sql

# Restore
psql -U node taxi_db_sec < backup_20260108.sql
```

## Monitoring & Logs

```bash
# View Gunicorn logs
sudo journalctl -u taxi_service -f

# View Nginx logs
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log
```

## Troubleshooting on Linux

### PostgreSQL Connection Issues

```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Check if port is listening
sudo netstat -nlp | grep 5432

# Check PostgreSQL config
sudo nano /etc/postgresql/*/main/postgresql.conf
sudo nano /etc/postgresql/*/main/pg_hba.conf

# Restart PostgreSQL
sudo systemctl restart postgresql
```

### Permission Issues

```bash
# Fix ownership
sudo chown -R $USER:$USER /home/$USER/taxi_service

# Fix static files
chmod -R 755 /home/$USER/taxi_service/static
chmod -R 755 /home/$USER/taxi_service/media
```

### Service Not Starting

```bash
# Check service status
sudo systemctl status taxi_service

# View detailed logs
sudo journalctl -xe

# Restart services
sudo systemctl restart taxi_service
sudo systemctl restart nginx
```

## SSL/HTTPS Setup (Let's Encrypt)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d your_domain.com

# Auto-renewal
sudo certbot renew --dry-run
```

## Quick Commands Reference

```bash
# Activate environment
source .venv/bin/activate

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static
python manage.py collectstatic --noinput

# Run tests
python manage.py test

# Load sample data
python manage.py load_sample_data

# Check for errors
python manage.py check

# Restart services
sudo systemctl restart taxi_service
sudo systemctl restart nginx

# View logs
sudo journalctl -u taxi_service -f
```

## Complete Deployment Checklist

- [ ] PostgreSQL installed and running
- [ ] Database `taxi_db_sec` created
- [ ] User `node` created with correct password
- [ ] Python virtual environment created
- [ ] Dependencies installed from requirements.txt
- [ ] .env file configured with production settings
- [ ] Migrations applied
- [ ] Superuser created
- [ ] Static files collected
- [ ] Gunicorn service configured and running
- [ ] Nginx configured and running
- [ ] Firewall rules set
- [ ] SSL certificate installed (optional)
- [ ] Database backup configured

## Done!

Your Taxi Service application should now be running on Linux with PostgreSQL!

