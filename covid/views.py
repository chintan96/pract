from django.shortcuts import render
from signup.models import *
import json
import requests
from django.http import JsonResponse
import datetime
import psutil
import plotly.graph_objects as go
import pycountry
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def get_data(request):
    if request.headers['token'] and request.method == "POST":
        api_token = request.headers['token'] ## api token must be passed through headers as 'token' for logged in users
        token = Token.objects.get(api_token=api_token) if Token.objects.filter(api_token=api_token).exists() else None
        data = json.loads(request.body.decode('utf-8'))
        if not token:
            response = {
                'message':'Bad request.'
            }
            return JsonResponse(response,status=400)
        user = token.user
        email = data['email'] if data['email'] else user.email # email to send to image of covid data
        country = data['country'] if data['country'] else user.profile.country #using default value
        country = pycountry.countries.get(name=country).alpha_2
        start_date = data['start_date']
        end_date = data['end_date']
        send_email = data['send_email'] # boolean value used to determine if an image has to be rendered and sent via email
        r = requests.get('http://corona-api.com/countries/'+country)
        if start_date and end_date:
            start_date = datetime.date.fromisoformat(start_date)
            end_date = datetime.date.fromisoformat(end_date)
        else: # default values
            end_date = datetime.date.today()
            start_date = end_date - datetime.timedelta(15)
        timeline = []
        flag = False
        for i in r.json()['data']['timeline']:
            if datetime.date.fromisoformat(i['date']) <= end_date and datetime.date.fromisoformat(i['date']) >= start_date:
                timeline.append(i)
                flag = True
            elif flag:# used to break out of the loop once the data from all the dates are collected, reducing overload
                break
        if send_email:
            fig = go.Figure(data=[go.Scatter(name='active',y=[s['active'] for s in timeline],x=[s['date'] for s in timeline]),go.Scatter(name='deaths',y=[s['deaths'] for s in timeline],x=[s['date'] for s in timeline]),go.Scatter(name='new confirmed',y=[s['new_confirmed'] for s in timeline],x=[s['date'] for s in timeline]),go.Scatter(name='new recovered',y=[s['new_recovered'] for s in timeline],x=[s['date'] for s in timeline]),go.Scatter(name = 'new deaths',y=[s['new_deaths'] for s in timeline],x=[s['date'] for s in timeline])])
            fig.write_image('figure.png')
            send_email_image(user.email,email,'figure.png')
        overall_data = r.json()['data']['latest_data']
        country_name = r.json()['data']['name']
        response = {
            'latest_data': overall_data,
            'given_timeline': timeline,
            'country': country_name,
            'message':'Data extraction successful.'
        }
        return JsonResponse(response,status=200)
    response = {
        'message':'Bad request.'
    }
    return JsonResponse(response,status=400)
