from django.db import models
from django.utils.translation import activate
from account.models import Profile


class Post(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,
                                related_name='posts')
    #likes
    #comments


    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.profile.user}: post {self.body[:10]}'

