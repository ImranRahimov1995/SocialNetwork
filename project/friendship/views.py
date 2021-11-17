from django.shortcuts import render
from .models import FriendshipRequest
from account.models import Profile
from django.contrib.auth.decorators import login_required


@login_required
def all_people(request):
    
    people = Profile.objects.exclude(user=request.user)

    context = {
        'people':people,
        'section':'People',
    }
    return render(request,'friendship/peoplepage.html',context)