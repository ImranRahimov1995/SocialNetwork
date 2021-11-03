from django.urls import path
from django.contrib.auth import views as av
from .views import *

urlpatterns = [
    #path('login/',user_login,name='login'),
    path('login/',av.LoginView.as_view(),name='login'),
    path('logout/',av.LogoutView.as_view(),name='logout'),
    path('',dashboard,name='dashboard'),
]