from rest_framework import generics
from .models import Chat
from .serializers import ChatSerializer

class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        sender_id = self.request.query_params.get('sender_id')
        receiver_id = self.request.query_params.get('receiver_id')
        
        if sender_id and receiver_id:
            return Chat.objects.filter(sender_id=sender_id, receiver_id=receiver_id)
        
        return Chat.objects.none()

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
