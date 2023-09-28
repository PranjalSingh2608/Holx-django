from django.urls import path
from .views import ChatListCreateView,ChatMessageListView

urlpatterns = [
    path('chat/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('chat-messages/', ChatMessageListView.as_view(), name='chat-message-list'),
]
