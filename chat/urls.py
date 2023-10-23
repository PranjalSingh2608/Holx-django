from django.urls import path
from .views import ChatListCreateView,ChatListView
urlpatterns = [
    path('', ChatListCreateView.as_view(), name='chat-list-create'),
    path('product/<int:product_id>/', ChatListView.as_view(), name='chat-list'),
]
