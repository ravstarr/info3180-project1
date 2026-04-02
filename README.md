# INFO3180 Project 1

Flask application for creating and viewing rental/sale properties stored in a PostgreSQL database.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app
flask db upgrade
flask --app app --debug run
```

## Features

- Add a new property with Flask-WTF
- Upload and store property photos
- View all properties
- View a single property
- Database migration included
