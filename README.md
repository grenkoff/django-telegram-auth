# Project `django-telegram-auth`

This project demonstrates user authentication via Telegram in a Django application using `django-rest-framework`, `social-auth-app-django`, and `drf-social-oauth2`.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)

---

## Features

- **Telegram Authentication**: Users can log in using Telegram.
- **REST API**: Includes a simple API for managing users.
- **OAuth2 Integration**: Handles authentication using `drf-social-oauth2`.
- **Bootstrap UI**: Basic frontend for interacting with the Telegram login widget.

---

## Technologies Used

- **Django 5.1.3**
- **Django REST Framework**
- **social-auth-app-django**
- **drf-social-oauth2**
- **Bootstrap 5**

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or later
- pip (Python package manager)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/grenkoff/django-telegram-auth.git
   cd django-telegram-auth
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

### Running the Project

Start the development server:

```bash
python manage.py runserver
```

Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

For demonstration purposes, you can click on the link to check the application's operation [https://f9c1-46-34-193-62.ngrok-free.app/](https://f9c1-46-34-193-62.ngrok-free.app/)