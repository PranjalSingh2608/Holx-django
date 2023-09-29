from django.urls import path
from .views import ChatListCreateView, ChatRoomListCreateView, ChatRoomRetrieveUpdateDestroyView

urlpatterns = [
    path('', ChatListCreateView.as_view(), name='chat-list-create'),
    path('chat-rooms/', ChatRoomListCreateView.as_view(), name='chat-room-list-create'),
    path('chat-rooms/<int:pk>/', ChatRoomRetrieveUpdateDestroyView.as_view(), name='chat-room-retrieve-update-destroy'),
]
