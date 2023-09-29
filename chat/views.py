from rest_framework import generics, permissions, status
from .models import Chat
from rest_framework.response import Response
from .serializers import ChatSerializer

class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        sender_id = self.request.user.id
        receiver_id = self.request.data.get('receiver_id')
        
        if receiver_id:
            serializer.save(sender_id=sender_id, receiver_id=receiver_id)
        else:
            return Response({"receiver_id": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        sender_id = self.request.query_params.get('sender_id')
        receiver_id = self.request.query_params.get('receiver_id')
        
        if sender_id and receiver_id:
            return Chat.objects.filter(sender_id=sender_id, receiver_id=receiver_id)
        
        return Chat.objects.none()
