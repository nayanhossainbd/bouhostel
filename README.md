🏠 BOU Hostel Management System

This repository hosts a comprehensive, university-level Hostel Management System developed as a project for academic purposes. It aims to digitize and streamline the administrative tasks associated with running a university residence hall, including student, room, and meal management.

✨ Features

The BOU Hostel Management System provides a centralized platform for efficient hostel administration with the following core functionalities:

👤 Student Management:

Enrollment and tracking of current and past hostel residents.

Detailed student profiles (contact, department, room history).

🛏️ Room & Allocation Management:

Real-time status of rooms (available, occupied, maintenance).

Efficient allocation and assignment of rooms to students.

🍽️ Meal/Food Management (Mess System):

Daily meal planning and menu scheduling.

Tracking of student attendance for meals (mess bill generation).

⚙️ Overall Hostel Administration:

Management of staff, utility bills, and financial records.

Reporting and insights for better administrative decision-making.

🚀 Technology Stack

This project is built using a robust and reliable web framework, primarily relying on the following technologies:

Category

Technology

Description

Backend

Python

The primary programming language.

Web Framework

Django

High-level Python web framework for rapid development.

Database

SQLite

Used for development and simple deployments.

Frontend

HTML5 & CSS3

Standard markup and styling for the user interface.

📦 Installation & Setup

Follow these steps to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites

You will need Python 3.x installed on your system.

1. Clone the Repository

git clone [https://github.com/nayanhossainbd/bouhostel.git](https://github.com/nayanhossainbd/bouhostel.git)
cd bouhostel


2. Set up Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

# Create and activate the virtual environment
python -m venv venv
source venv/bin/activate  # On Linux/macOS
# or .\venv\Scripts\activate # On Windows


3. Install Dependencies

Install the required packages. This project primarily uses Django.

# Install Django and any other necessary packages (e.g., pillow, python-decouple)
pip install django


4. Database Setup

Apply database migrations to set up the necessary tables:

python manage.py makemigrations
python manage.py migrate


5. Create a Superuser

Create an administrator account to access the Django admin panel:

python manage.py createsuperuser


6. Run the Application

Start the development server:

python manage.py runserver


The application should now be running at http://127.0.0.1:8000/.

🤝 Contribution

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your Changes (git commit -m 'feat: Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📄 License

Distributed under the MIT License. See LICENSE for more information (if you plan to add one).

📞 Contact

Nayan Hossain -

Project Link: https://github.com/nayanhossainbd/bouhostel
