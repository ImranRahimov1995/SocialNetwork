from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,PublicStatus
from .forms import *
from django.contrib import messages


@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    public_status =  PublicStatus.objects.get(owner=profile)
    return render(request,'dashboard.html',{'section':'dashboard',
                                            'profile':profile,
                                            'public_status':public_status,
                                            })


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            #Create new profile with new user
            profile = Profile.objects.create(user=new_user)
            PublicStatus.objects.create(owner=profile)
            return render(request,'account/register_done.html',
                                        {'new_user':new_user,})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form':user_form,})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST, 
                                       files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            messages.success(request, 'Profile updated successfully')
            
            user_form.save()
            profile_form.save()
            
            return  redirect('dashboard')
        else:
             messages.error(request, 'Error updating your profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })