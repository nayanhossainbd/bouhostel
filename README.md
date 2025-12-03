# 🌐 BOU Hostel Management System  
*A University-Level Digital Hostel Administration Platform*

![GitHub repo size](https://img.shields.io/github/repo-size/nayanhossainbd/bouhostel?color=blue)
![GitHub stars](https://img.shields.io/github/stars/nayanhossainbd/bouhostel?style=social)
![GitHub forks](https://img.shields.io/github/forks/nayanhossainbd/bouhostel?style=social)
![GitHub License](https://img.shields.io/github/license/nayanhossainbd/bouhostel)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

---

## 📘 Overview

The **BOU Hostel Management System** is a comprehensive university-level digital platform designed to modernize and streamline hostel administration tasks.  
Developed for academic purposes, it simplifies the management of **students, rooms, meals, billing, and administrative operations**.

---

## ✨ Features

### 👤 Student Management
- Enrollment and tracking of current & past hostel residents  
- Complete student profiles (contact details, department, ID)  
- Room history & allocation records  

### 🛏️ Room & Allocation Management
- Real-time room status (Available / Occupied / Maintenance)  
- Efficient room assignment workflow  
- Hostel capacity monitoring  

### 🍽️ Meal / Mess System
- Daily menu creation  
- Meal attendance tracking  
- Automatic mess bill calculation  

### ⚙️ Hostel Administration Tools
- Staff and utility bill management  
- Expense & financial tracking  
- Administrative reports and insights  

---

## 🚀 Technology Stack

| Category        | Technology      | Description                                      |
|-----------------|------------------|--------------------------------------------------|
| **Backend**     | Python           | Core programming language                        |
| **Framework**   | Django           | High-level Python web framework                  |
| **Database**    | SQLite           | Default database for development                 |
| **Frontend**    | HTML5 & CSS3     | Standard web UI technologies                     |

---

## 📦 Installation & Setup

### **Prerequisites**
Ensure you have:
- **Python 3.x**
- (Recommended) A virtual environment system like `venv`

---

### **1. Clone the Repository**
```bash
git clone https://github.com/nayanhossainbd/bouhostel.git
cd bouhostel
```
2. Create & Activate Virtual Environment
```
python -m venv venv
source venv/bin/activate       # Linux/macOS

# OR (for Windows)
.\venv\Scripts\activate
```
3. Install Dependencies
```
pip install django

(Install additional packages as needed: pillow, python-decouple, etc.)
```
4. Database Setup
```
Run migrations:

python manage.py makemigrations
python manage.py migrate

```
5. Create Superuser
```
python manage.py createsuperuser
```
7. Run the Application
```
python manage.py runserver
```

Visit the application at:
```
👉 http://127.0.0.1:8000/
```
🤝 Contribution

Contributions are welcome and appreciated!

