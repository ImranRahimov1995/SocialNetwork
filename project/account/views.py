from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile,PublicStatus
from .forms import *
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from posts.models import Post


# in developing|security faulth
@require_http_methods(["GET"])
def profile_detail(request,pk):
    profile = get_object_or_404(Profile,user=pk)
    public_status =  PublicStatus.objects.get(owner=profile)
    return render(request,'account/profile_detail.html',{ ######,
                                            'profile':profile,
                                            'public_status':public_status,
                                            })


@login_required
def dashboard(request):
    profile = get_object_or_404(Profile,user=request.user)
    public_status =  PublicStatus.objects.get(owner=profile)
    posts = Post.objects.filter(active=True,profile=profile).order_by('-created')
    return render(request,'account/dashboard.html',{ 'section':'Profile',
                                            'profile':profile,
                                            'public_status':public_status,
                                            'posts':posts,
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
    """Profile edit"""
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