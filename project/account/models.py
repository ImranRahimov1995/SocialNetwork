from django.db import models
from django.conf import settings
from django.urls import reverse





class Profile(models.Model):
    """
    This model will be created every time when user registration pass.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE,
                                related_name='profile')
                                
    #following = models.ManyToManyField('self',through='friendship.FriendshipRequest',related_name="friends",symmetrical=False)
    # objects = models.Manager()
    # friends = FriendsListManager()

    date_of_birth = models.DateField(blank=True,null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    city = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
    
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
    
    def get_friends(self):
        my_friends = []

        fr = self.fr_request.filter(accepted=True)
        sended_frs = self.sended_fr_request.filter(accepted=True)

        if fr:
            my_friends.append(*fr)
            # if sended_frs:
            #     my_friends.append(*sended_frs)
        if sended_frs:
            my_friends.append(*sended_frs)
        return my_friends
    
    def get_friend_requests(self):
        return self.fr_request.all()

    def get_sended_requests(self):
        return self.sended_fr_request.all()



class PublicStatus(models.Model):
    owner = models.OneToOneField(Profile,on_delete=models.CASCADE)
    status_text = models.CharField(max_length=250,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.owner.user} status created at: {self.created}" 

