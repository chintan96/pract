from django.urls import path
from . import views

app_name = 'signup'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_off/', views.sign_off, name='sign_off'),
]
