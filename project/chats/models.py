from django.db import models
from django.urls import reverse

from account.models import Profile


class Chat(models.Model):
    members = models.ManyToManyField(Profile,
                                     related_name='chat')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('chat_detail', kwargs={'pk': self.pk, })

    class Meta:
        ordering = ('-created_at',)


class Message(models.Model):
    author = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               related_name='sent_message')

    recipient = models.ForeignKey(Profile,
                                  on_delete=models.CASCADE,
                                  related_name='delivered_message')
    chat = models.ForeignKey(Chat,
                             on_delete=models.CASCADE,
                             related_name='all_messages',
                             null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        ordering = ('-created_at',)
