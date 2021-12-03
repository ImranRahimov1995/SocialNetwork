from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('chats/<pk>/',views.ChatApiView.as_view()),
    path('create/',views.CreateMessageView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)