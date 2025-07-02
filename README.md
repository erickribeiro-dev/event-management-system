# event-management-system
A Django system for creating and managing events.

> ⚠️ **This project is currently in development.** Features may change, and full functionality is not yet ready.

## Table of Contents
- [Features](#features)
- [Technologies used](#technologies-used)
- [Setup instructions (Windows)](#setup-instructions-windows)

## Features
- Event management: Create and manage Events with categories, images, tags, location, featured badges, price, and more.
- Ticket management: Create and manage Tickets, capacity, price, ticket types (early bird, standard, VIP), QR code, and more.
- User authentication: Secure user authentication and forms.
- Responsive design: Modern user interface developed with Bootstrap 5.3, adaptative to phones, tables, and all screen sizes.

## Technologies used
- Python 3.13.5
- Django 5.2.4
- Bootstrap 5.3.7
- SQLite (temporary, will use PostgreSQL later)

## Setup instructions (Windows)
0. Create a directory for the project.

1. Clone this repository:
```bash
git clone https://github.com/erickribeiro-dev/event-management-system.git
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\activate
```
- Note: Remember to always activate this virtual environment when coming back to this project to work on it.

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Database migration:
```bash
python manage.py migrate
```

5. Generate a SECRET_KEY:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
- Alternatively, generate a SECRET_KEY from Python Shell:
```bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

6. Set up SECRET_KEY environment variable:
- On Windows, open "View advanced system settings (Control Panel)"
- In the "System Properties'" Advanced tab, click "Environment Variables..."
- Under System variables click "New...", and enter the values, then press OK:
- Variable name: EMS_SECRET_KEY
- Variable value: \<your secret key\>

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Create a static folder and download bootstrap 5.3.7:
```bash
mkdir static\vendor\bootstrap
```
- Download bootstrap [here](https://getbootstrap.com/docs/5.3/getting-started/download/)
- Extract the .zip file
- Move the entire css/ and js/ folders to the "static/vendor/bootstrap" directory created

9. Run the development server:
```bash
python manage.py runserver
```

10. To access the Django admin dashboard:
- Go to 127.0.0.1:8000/admin
- Enter the superuser credentials you created on step 7