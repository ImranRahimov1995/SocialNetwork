from django.shortcuts import render
from account.models import Profile
from django.contrib.auth.decorators import login_required


@login_required
def all_people(request):
    
    profiles = Profile.objects.exclude(user=request.user)

    context = {
        'profiles':profiles,
        'section':'People',
    }

    return render(request,'friendship/peoplepage.html',context)