from django.db import models
from account.models import Profile
from django.core.exceptions import ValidationError


class Friends(models.Model):
    user1 = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='user1_rel',
    )

    user2 = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='user2_rel',
    )

    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        unique_together = ('user1', 'user2')


class FriendshipRequest(models.Model):
    user_from = models.ForeignKey(
        Profile,
        related_name='sent_requests',
        on_delete=models.CASCADE
    )

    user_to = models.ForeignKey(
        Profile,
        related_name='received_requests',
        on_delete=models.CASCADE
    )

    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        unique_together = ('user_from', 'user_to')

    def __str__(self):
        return f"{self.user_from}" \
               f" send friendship {self.user_to}"

    def save(self, *args, **kwargs):

        if self.user_from == self.user_to:
            return ValidationError('cant do this')

        check = self.__class__.objects.filter(
            user_from=self.user_to,
            user_to=self.user_from
        )

        if check:
            return ValidationError('Already exists')

        super().save(*args, **kwargs)

        if self.accepted == True:
            Friends.objects.create(
                user1=self.user_from,
                user2=self.user_to,
            )
            Friends.objects.create(
                user1=self.user_to,
                user2=self.user_from,
            )
