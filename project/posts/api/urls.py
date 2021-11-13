from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('create/', 
         views.PostCreateView.as_view()),
    path('get/<pk>', 
         views.PostRetrieveView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)