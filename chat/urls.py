from django.urls import path
from .views import ChatListCreateView

urlpatterns = [
    path('', ChatListCreateView.as_view(), name='chat-list-create'),
    path('<int:sender_id>/<int:receiver_id>/', ChatListCreateView.as_view(), name='chat-list-by-sender-receiver'),
]
