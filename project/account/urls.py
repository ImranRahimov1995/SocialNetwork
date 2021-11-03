from django.urls import path,include
from django.contrib.auth import views as av
from .views import *

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #main
    path('',dashboard,name='dashboard'),
]