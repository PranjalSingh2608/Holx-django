from rest_framework import generics
from .models import Chat
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ChatSerializer

class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    @action(detail=False, methods=['GET'])
    def chat_history(self, request):
        sender_id = request.query_params.get('sender_id')
        receiver_id = request.query_params.get('receiver_id')
        
        if sender_id and receiver_id:
            chats = Chat.objects.filter(sender_id=sender_id, receiver_id=receiver_id)
            serializer = ChatSerializer(chats, many=True)
            return Response(serializer.data)
        
        return Response([])
