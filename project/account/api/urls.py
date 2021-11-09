from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('status/get/<owner>/', csrf_exempt(views.PublicStatusRetrieveView.as_view())),
]

urlpatterns = format_suffix_patterns(urlpatterns)