from django.shortcuts import render
import uuid
import json
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        country = data['country']
        password = data['password']
        token = str(uuid.uuid4())
        if first_name and last_name and email and country and password:
            user = User.objects.create_user(username=email,email=email,password=password,first_name=first_name,last_name=last_name)
            profile = Profile.objects.get(user=user)
            token = Token.objects.get(user)
            profile.country = country
            token.api_token = token
            token.is_enabled = True
            user.save()
            profile.save()
            token.save()
            response = {
                'token': api_token,
                'message':'Sign up successful.'
            }
            return JsonResponse(response,status=200)
        response = {
            'token': None,
            'message':'Sign up unsuccessful.'
        }
        return JsonResponse(response,status=206)
    response = {
        'token': None,
        'message':'Sign up requires POST requests.'
    }
    return JsonResponse(response,status=403)

@csrf_exempt
def sign_off(request):
    if request.headers['token'] and request.method == "POST":
        api_token = request.headers['token'] ## api token must be passed through headers as 'token' for logged in users
        token = Token.objects.get(api_token=api_token) if Token.objects.filter(api_token=api_token).exists() else None
        if not token:
            response = {
                'message':'Bad request.'
            }
            return JsonResponse(response,status=400)
        if token.is_enabled:
            token.is_enabled = False
            token.api_token = None
            token.save()
            response = {
                'message':'Sign off successful.'
            }
            return JsonResponse(response,status=200)
        response = {
            'message':'User already signed off.'
        }
        return JsonResponse(response,status=200)
    response = {
        'message':'Bad request.'
    }
    return JsonResponse(response,status=400)
