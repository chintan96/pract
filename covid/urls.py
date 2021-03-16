from django.urls import path
from . import views

app_name = 'covid'

urlpatterns = [
    path('get_data/', views.get_data, name='get_data'),
]
