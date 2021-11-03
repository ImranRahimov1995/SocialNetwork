from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


@login_required
def dashboard(request):
    return render(request,'dashboard.html',{'section':'dashboard',})
