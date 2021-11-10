from django.urls import path,include
from django.contrib.auth import views as av
from .views import *

urlpatterns = [
    #auth reg
    path('register/',register,name='register'),
    path('edit/',edit,name='edit'),
    path('', include('django.contrib.auth.urls')),
    #main
    path('api/profile/',include('account.api.urls',)),

    path('profile/<int:pk>/',profile_detail,name='profile_detail'),
    path('',dashboard,name='dashboard'),
]
