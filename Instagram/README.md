 ## Instagram
Instagram is the garelly website where user have to create account and can upload image,receive others image like or dislike, have the number of followers and following and can also make a comments.
## By MUKASINE Marie Claire

## Specifications
user have to signup after signup,it automatically receive a login button where he have to put the name and password and then the user have an account where he/she can uploads image, views different image posted by other he/she can like or dislike follow or make a comments

## Set Up and Installations
Prerequisites
* Ubuntu Software
* Python3.6
* Postgres
* python virtualenv
* Clone the Repo
Run the following command on the terminal: git clone https://github.com/mukasine/instagram.git && cd instagram

## Activate virtual environment
Activate virtual environment using python3.6 as default handler

* virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
* Install dependancies
* Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## Create the Database
* psql
* CREATE DATABASE insto;
## env file
Create .env file and paste the following:

SECRET_KEY = '<Secret_key>'
DBNAME = 'insto'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'

## Run initial Migration

python3.6 manage.py check
python manage.py makemigrations instagram
python3.6 manage.py sqlmigrate instagram 0001
python3.6 manage.py migrate

## Run the app

python3.6 manage.py runserver
copy: http://127.0.0.1:8000/ past to the browser

## Known bugs

Like and Follow functionality do not work

## Technologies used

- Python 3.6
- HTML for the structure
- Bootstrap 4 for the design
- JavaScript
- Heroku for the deployment
- Postgresql for the database

## Support and contact details

* for any support please contact me on mclaremukasine@gmail.com or
* phone:0782586013 

## License
[MIT](https://choosealicense.com/licenses/mit/)
Copyright (c) 2019 **MUKASINE Marie Claire**
