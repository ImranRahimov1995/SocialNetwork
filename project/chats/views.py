from django.shortcuts import render


def get_chats(request):
    context = {
        'section': 'Messages',
    }

    return render(request,'chats/chats.html',context)