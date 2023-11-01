from django.urls import path
from .views import ChatListCreateView,ChatListView,fetch_chat_messages_by_receiver_id
urlpatterns = [
    path('create/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('product/<int:product_id>/sender/<int:sender_id>/receiver/<int:receiver_id>/', ChatListView.as_view(), name='chat-list'),
    path('fetch/<int:receiver_id>/',fetch_chat_messages_by_receiver_id, name='fetch_chat_by_receiver_id'),
]
