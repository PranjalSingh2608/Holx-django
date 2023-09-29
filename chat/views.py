from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status

from application.models import Products
from .models import Chat, ChatRoom
from rest_framework.response import Response
from .serializers import ChatRoomSerializer, ChatSerializer

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


class ChatRoomListCreateView(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        product_id = self.request.data.get('product_id')
        product = get_object_or_404(Products, id=product_id)

        if product.owner == self.request.user:
            serializer.save(product=product, members=[self.request.user])
        else:
            return Response(
                {'error': 'You are not the owner of this product.'},
                status=status.HTTP_403_FORBIDDEN
            )

class ChatRoomRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        chat_room = self.get_object()
        if request.user in chat_room.members.all():
            return super().put(request, *args, **kwargs)
        else:
            return Response(
                {'error': 'You are not a member of this chat room.'},
                status=status.HTTP_403_FORBIDDEN
            )

    def delete(self, request, *args, **kwargs):
        chat_room = self.get_object()
        if request.user in chat_room.members.all():
            return super().delete(request, *args, **kwargs)
        else:
            return Response(
                {'error': 'You are not a member of this chat room.'},
                status=status.HTTP_403_FORBIDDEN
            )






