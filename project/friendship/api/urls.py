from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('add/',views.FriendshipRequestCreateView.as_view()),
    path('get/<pk>/',views.FriendshipRequestRetrieveView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)