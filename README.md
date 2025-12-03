# BOUHostel — University Hostel Management System 🏠

**BOUHostel** is a university-level hostel management system originally built by **nayanhossainbd**.  
It aims to digitize and streamline hostel administration: managing students, rooms, meals, and overall hostel operations.

## 🚀 Features

- Student / resident management (profiles, room history, etc.)  
- Room allocation and status tracking (available, occupied, maintenance)  
- Meal / mess management: daily meal scheduling and attendance tracking  
- Meal billing and mess fee management (if configured)  
- Utility bills and financial record management  
- Reporting and administrative tools for hostel staff  
- Web-based interface using Django + HTML/CSS  

## 🧰 Technology Stack

| Layer            | Tech / Framework            |
|------------------|-----------------------------|
| Backend          | **Python** + **Django**      |
| Database         | SQLite (default)            |
| Frontend         | HTML5 & CSS3                |

*(Note: The project appears to be using SQLite by default, but can be adapted to other DBs per Django’s configuration.)*

## 📦 Installation & Setup Guide

To get the project running locally:

```bash
git clone https://github.com/nayanhossainbd/bouhostel.git
cd bouhostel

# (Optionally) create & activate a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: .\venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt  # or install Django manually

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# (Optional) Create a superuser for Django admin
python manage.py createsuperuser

# Start the development server
python manage.py runserver
