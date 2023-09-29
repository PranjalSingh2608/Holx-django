from django.db import models
from django.contrib.auth.models import User

from application.models import Products

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sent_chats')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name='recieved_chats')
    product = models.ForeignKey(Products, on_delete=models.CASCADE,default='23')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} to {self.receiver.username}"
