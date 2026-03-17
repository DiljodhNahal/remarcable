# Remarcable Django Take-Home Coding Assignment
Dil Nahal\
diljodhnahal@hotmail.com

## System Requirements
- Python 3.12+
- Django 6.0+

## Setup
```bash
# Clone Repository
git clone <repo-url>
cd remarcable

# Create & Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Generate Default .env File
python manage.py generate_env

# Run Migrations
python manage.py migrate
```

##  Data
As required by the assignment instructions, the data on the demo site was loaded manually using the Django Admin Interface.

For your own testing, you can populate the database with test data using the following custom management command.
```bash
python manage.py populate_db
```

## Running Server
```bash
python manage.py runserver
```

## Local Admin Access
To view the Django Administration Panel locally, type the following command
```bash
python manage.py createsuperuser
```
By following the prompts, you will be able to create your local administrator account.
You can view the local Django Administration Panel at http://127.0.0.1:8000/admin once your local server is running.


## Demo Site
The demo site with pre-populated data can be viewed at https://dilnahal.pythonanywhere.com/.

The Django Administration Panel is available at https://dilnahal.pythonanywhere.com/admin and can be accessed using the provided administrator username and password (see text document attached to submission).

## AI Attribution
Claude Opus 4.6 was used to generate sample data to populate the db and quickly reference Django & Bootstrap documentation.
