from rest_framework import serializers
from .models import Chat
from django.contrib.auth.models import User

class ChatSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Chat
        fields = '__all__'

    def create(self, validated_data):
        sender_id = validated_data.pop('sender')
        receiver_id = validated_data.pop('receiver')
        chat = Chat(sender=sender_id, receiver=receiver_id, **validated_data)
        chat.save()
        return chat
