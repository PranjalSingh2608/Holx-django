from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status,filters

from application.models import Products
from .models import Chat
from rest_framework.response import Response
from .serializers import ChatSerializer
from  rest_framework.authentication import TokenAuthentication

class ChatListCreateView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    # def perform_create(self, serializer):
    #     sender_id = self.request.user.id
    #     receiver_id = self.request.data.get('receiver_id')
        
    #     if receiver_id:
    #         serializer.save(sender_id=sender_id, receiver_id=receiver_id)
    #     else:
    #         return Response({"receiver_id": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)


class ChatListView(generics.ListAPIView):
    serializer_class=ChatSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        product_id=self.kwargs['product_id']
        sender_id = self.kwargs['sender_id']
        receiver_id = self.kwargs['receiver_id']
        return Chat.objects.filter(product_id=product_id,sender_id=sender_id, receiver_id=receiver_id)



def fetch_chat_by_receiver_id(request, receiver_id):
    chat_messages = Chat.objects.filter(receiver=receiver_id)

    serialized_chat_messages = [
        {
            'id': message.id,
            'sender': message.sender,
            'message': message.message,
            'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),  
        }
        for message in chat_messages
    ]
    return JsonResponse({'chat_messages': serialized_chat_messages})