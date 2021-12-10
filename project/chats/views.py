from django.shortcuts import render
from .models import Chat


def get_chats(request):
    my_profile = request.user.profile
    chats = my_profile.chat.all().order_by('-updated_at')

    context = {
        'section': 'Messages',
        'chats': chats,
        'profile': my_profile,
    }

    return render(request, 'chats/chats.html', context)
