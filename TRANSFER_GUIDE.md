# HOW TO TRANSFER TO LINUX

## Option 1: Create Archive (Recommended)

### On Windows:

1. Delete `.venv` folder (it will be recreated on Linux):
   ```
   Remove-Item -Recurse -Force .venv
   ```

2. Create ZIP archive:
   ```
   Compress-Archive -Path * -DestinationPath taxi_service.zip
   ```

3. Transfer `taxi_service.zip` to Linux using:
   - SCP: `scp taxi_service.zip user@linux-server:/home/user/`
   - FileZilla, WinSCP, or any SFTP client
   - USB drive if physical access

### On Linux:

1. Extract:
   ```bash
   unzip taxi_service.zip -d taxi_service
   cd taxi_service
   ```

2. Run automated setup:
   ```bash
   chmod +x setup.sh
   bash setup.sh
   ```

3. Create superuser:
   ```bash
   source .venv/bin/activate
   python manage.py createsuperuser
   ```

4. Start server:
   ```bash
   bash run.sh
   ```

## Option 2: Git (If using Git)

### On Windows:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_REPO_URL
git push -u origin main
```

### On Linux:
```bash
git clone YOUR_REPO_URL
cd taxi_service
bash setup.sh
```

## Option 3: Direct Copy

Copy entire `taxi_service` folder (except `.venv`) to Linux.

## Files Included

- ✅ All source code
- ✅ Database configuration (.env)
- ✅ Templates and static files
- ✅ Requirements.txt
- ✅ Setup scripts (setup.sh, run.sh)
- ✅ Documentation (README.md, QUICKSTART.md, etc.)
- ✅ Tests
- ✅ Sample data loader

## What Happens on Linux

The `setup.sh` script will:
1. Install Python, PostgreSQL
2. Create database `taxi_db_sec`
3. Create user `node` with password `9562`
4. Install Python packages
5. Run migrations
6. Load sample data
7. Run tests

## After Setup

Access your application at:
- **Main site**: http://YOUR_SERVER_IP:8000
- **Admin**: http://YOUR_SERVER_IP:8000/admin

Sample accounts:
- Riders: john@rider.com / password123
- Drivers: mike@driver.com / password123

## Need Help?

- QUICKSTART.md - Quick setup guide
- README.md - Full documentation
- LINUX_DEPLOYMENT.md - Production deployment
- CHECKLIST.md - Features checklist

