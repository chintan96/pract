# pract
Practical Task Backend

Python 3.8.5 / Django 3.1 was used to create this project on Ubuntu 20.04 LTS machine in a virtual environment.
Rest of the requirements can be found in requirements.txt

Steps:
Install Python 3.8.5
Create a virtualenv/venv from python3.8.5
Activate venv
Install all the requirements from requirements.txt
Run the project




Additional Information:
Django's internal user model was used to create user, additional data was stored in another models related to origianal user model.

Celery has been used to perform background task of sending image via email.

Plotly's scatter plot has been used to plot covid data.

Pycountry used to determine ISO alpha_2 value of a country, in order to access covid-data api.

Please make sure to insert your password in covid/tasks.py file for email to work.

An assumption has been made that data coming from frontend has been validated.

Usually most codes are confined inside try catch cases, it has not been implemented here for clear cut frontend and backend debugging.
