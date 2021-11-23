from django.urls import path
from . import views

app_name = 'friendship'

urlpatterns = [
    path('',views.all_people ,name='people'),
]
