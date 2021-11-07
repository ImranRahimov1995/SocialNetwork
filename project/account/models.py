from django.db import models
from django.conf import settings

class Profile(models.Model):
    """
    This model will be created every time when user registration pass.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True,null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    city = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


class PublicStatus(models.Model):
    owner = models.OneToOneField(Profile,on_delete=models.CASCADE)
    status_text = models.CharField(max_length=250)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.owner.user} status created at: {self.created}" 

