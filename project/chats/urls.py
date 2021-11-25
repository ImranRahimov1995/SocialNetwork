from django.urls import path
from . import views

app_name = 'chats'

urlpatterns = [
    path('',views.get_chats ,name='all_chats'),
]