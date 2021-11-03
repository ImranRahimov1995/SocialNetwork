from django.shortcuts import render
from django.http import HttpResponse

from .forms import LoginForm
from .services import check_user_auth
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request,'dashboard.html',{'section':'dashboard',})

#def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            check = check_user_auth(request,cleaned_data=form.cleaned_data)
            if check:
                if check == 'Disabled account':
                    return HttpResponse(check)
                return HttpResponse(f'good job {request.user}')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form,})
