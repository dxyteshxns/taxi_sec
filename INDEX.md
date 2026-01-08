# 🚕 Taxi Service - Complete Django Application

## 📚 Documentation Index

This project includes complete documentation for deployment and usage:

### 🚀 Getting Started

1. **QUICKSTART.md** - Fastest way to get up and running
   - One-command setup for Linux
   - Sample accounts
   - Basic commands

2. **TRANSFER_GUIDE.md** - How to transfer from Windows to Linux
   - Archive creation
   - Transfer methods
   - Extraction instructions

### 📖 Full Documentation

3. **README.md** - Complete project documentation
   - Full feature list
   - Detailed installation steps
   - Project structure
   - API endpoints
   - Troubleshooting

4. **LINUX_DEPLOYMENT.md** - Production deployment guide
   - Gunicorn setup
   - Nginx configuration
   - SSL/HTTPS setup
   - Service management
   - Monitoring

5. **CHECKLIST.md** - Project completion checklist
   - All implemented features
   - Database schema
   - Testing coverage
   - Deployment readiness

### 🛠️ Scripts

6. **setup.sh** - Automated Linux setup script
   - Installs all dependencies
   - Creates database
   - Runs migrations
   - Loads sample data

7. **run.sh** - Quick server start script
   - Activates environment
   - Checks database
   - Starts development server

8. **prepare_for_linux.ps1** - Windows preparation script
   - Cleans project
   - Creates archive
   - Ready for transfer

## 📁 Project Structure

```
taxi_service/
├── 📄 Documentation
│   ├── README.md                 # Main documentation
│   ├── QUICKSTART.md            # Quick start guide
│   ├── LINUX_DEPLOYMENT.md      # Production guide
│   ├── TRANSFER_GUIDE.md        # Transfer instructions
│   ├── CHECKLIST.md             # Feature checklist
│   └── INDEX.md                 # This file
│
├── 🔧 Configuration
│   ├── requirements.txt         # Python dependencies
│   ├── .env                     # Environment config
│   ├── .env.example            # Config template
│   ├── .gitignore              # Git ignore rules
│   ├── .flake8                 # Flake8 config
│   ├── .pre-commit-config.yaml # Pre-commit hooks
│   └── pyproject.toml          # Tool configuration
│
├── 🚀 Scripts
│   ├── setup.sh                # Linux auto-setup
│   ├── run.sh                  # Quick server start
│   ├── prepare_for_linux.ps1   # Archive creator
│   └── manage.py               # Django management
│
├── 💻 Applications
│   ├── accounts/               # User authentication
│   ├── trips/                  # Trip management
│   ├── vehicles/               # Vehicle management
│   └── taxi_project/           # Main project
│
├── 🎨 Frontend
│   ├── templates/              # HTML templates
│   └── static/                 # CSS, JavaScript
│
└── 📦 Data
    └── media/                  # User uploads
```

## 🎯 Quick Commands

### On Windows
```powershell
# Prepare for Linux
.\prepare_for_linux.ps1
```

### On Linux
```bash
# First time setup
bash setup.sh

# Start server
bash run.sh

# Or manually
source .venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

## ✨ Features

- ✅ User registration (Rider/Driver)
- ✅ Trip ordering and tracking
- ✅ Driver acceptance system
- ✅ Vehicle management
- ✅ Rating system
- ✅ Admin panel
- ✅ Responsive UI (Bootstrap 5)
- ✅ PostgreSQL database
- ✅ Sample data
- ✅ Unit tests

## 🔗 URLs

- **Home**: /
- **Register**: /accounts/register/
- **Login**: /accounts/login/
- **Profile**: /accounts/profile/
- **Trips**: /trips/
- **Create Trip**: /trips/create/
- **Available Trips**: /trips/available/
- **Vehicles**: /vehicles/
- **Admin**: /admin/

## 🗄️ Database

**PostgreSQL Configuration:**
- Database: taxi_db_sec
- User: node
- Password: 9562
- Host: localhost
- Port: 5432

## 👥 Sample Accounts

After running `python manage.py load_sample_data`:

**Riders:**
- john@rider.com / password123
- jane@rider.com / password123

**Drivers:**
- mike@driver.com / password123
- sarah@driver.com / password123

## 📝 Development

```bash
# Run tests
python manage.py test

# Format code
black .
isort .

# Check code quality
flake8

# Make migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data
python manage.py load_sample_data
```

## 🐛 Troubleshooting

1. **Database connection error**
   - Check PostgreSQL is running: `sudo systemctl status postgresql`
   - Verify .env credentials

2. **Module not found**
   - Activate venv: `source .venv/bin/activate`
   - Install deps: `pip install -r requirements.txt`

3. **Migration issues**
   - Delete migrations folders
   - Run: `python manage.py makemigrations`
   - Run: `python manage.py migrate`

## 📞 Support

- Check documentation files listed above
- Run: `python manage.py check`
- View logs for errors

## 🎓 Tech Stack

- **Backend**: Django 4.2+
- **Database**: PostgreSQL
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Python**: 3.10+
- **Tools**: Black, Flake8, isort

## 📜 License

Educational purposes

---

**🚕 Ready to deploy on Linux with PostgreSQL!**

For the fastest start: **Read QUICKSTART.md**

