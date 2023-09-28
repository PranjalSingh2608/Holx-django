from django.urls import path
from .views import ChatListCreateView

urlpatterns = [
    path('chat/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('chat_history/', ChatListCreateView.as_view({'get': 'chat_history'}), name='chat-history'),
]
