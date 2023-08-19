from rest_framework import generics,permissions
from .models import Products
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from  rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

product_list_create_view=ProductCreateAPIView.as_view()


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


    def get_queryset(self):
        return Products.objects.all()

product_alter_view=ProductRetrieveUpdateDestroyAPIView.as_view()    

