# Iranian Pooshesh
This is a sample project. It has been developed only for challenge of Iranian Pooshesh Company.

## Iranian Pooshesh core based on:

- Python 3.11 version
- Django 4.2 version

## How to Download:

```bash
git clone git@github.com:baratihd/iranian-pooshesh.git
```
or
```bash
git clone https://github.com/baratihd/iranian-pooshesh.git
```

## How to start:

### Install dependencies:

Create virtualenv
```bash
python3 -m venv venv
```

Active virtualenv
```bash
source venv/bin/activate
```

Install packages
```bash
pip install -r requirements.txt
```

### Run project:
Create database:
```bash
python manage.py migrate
```

Run project:
```bash
python manage.py runserver
```

Access swagger:
```html
http://localhost:8000/schema/swagger/
```
