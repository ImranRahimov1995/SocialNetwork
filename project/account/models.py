from django.db import models
from django.conf import settings
from django.urls import reverse


def get_avatar_place(instance, filename):
    return f'users/{instance.user}/avatar/{filename}'


class Profile(models.Model):
    """
    This model will be created every time when user registration pass.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')

    friends = models.ManyToManyField(
        'self',
        through='friendship.Friends',
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=get_avatar_place, blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.pk = self.user.pk
        super().save(*args, **kwargs)


class PublicStatus(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=250, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner.user} status created at: {self.created}"
