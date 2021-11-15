from django.db import models
from account.models import Profile




class FriendshipRequest(models.Model):

    user_from = models.ForeignKey(Profile,related_name='sended_fr_request',on_delete=models.CASCADE)
    user_to = models.ForeignKey(Profile,related_name='fr_request',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,db_index=True)

    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.user_from} send friendship {self.user_to}"


    