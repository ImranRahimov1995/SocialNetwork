from django.shortcuts import render
from .models import FriendshipRequest
from account.models import Profile



def all_people(request):
    peoples = Profile.objects.all()

    context = {
        'peoples':peoples,
        'section':'People',
    }
    return render(request,'friendship/peoplepage.html',context)