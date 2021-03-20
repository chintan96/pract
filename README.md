# pract
Practical Task Backend

Python 3.8.5 / Django 3.1 was used to create this project on Ubuntu 20.04 LTS machine in a virtual environment.
Rest of the requirements can be found in requirements.txt.

Steps:
Install Python 3.8.5.
Create a virtualenv/venv from python3.8.5.
Activate venv.
Install all the requirements from requirements.txt.
Run the project.



How to:
for sign up visit "/api/signup/sign_up/" with body containing json data of "first_name", "last_name", "email", "country" and "password"
after signup a token will be returned which shall be used as API Token.

for covid data visit "api/covid/get_data/" with header containing api token as "token" and body containing json data of "email"(email to send image to), "country", "start_date" and "end_date" in ISO format and a boolean value "send_email" to determine if an email has to be send or not.




Additional Information:
Django's internal user model was used to create user, additional data was stored in another models related to origianal user model.

Celery has been used to perform background task of sending image via email.

Plotly's scatter plot has been used to plot covid data.

Pycountry used to determine ISO alpha_2 value of a country, in order to access covid-data api.

Please make sure to insert your password in covid/tasks.py file for email to work.

An assumption has been made that data coming from frontend has been validated.

Usually most codes are confined inside try catch cases, it has not been implemented here for clear cut frontend and backend debugging.
