from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #local
    path('admin/', admin.site.urls),
    #posts
    path('api/posts/',include('posts.api.urls'),),
    #people
    path('people/',include('friendship.urls'),),
    path('api/people/',include('friendship.api.urls',),),
    #profile
    path('',include('account.urls',)),
]

#local settings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)