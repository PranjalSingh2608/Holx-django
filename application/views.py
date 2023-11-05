from rest_framework import generics,permissions
from .models import Products
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from  rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get_queryset(self):
        user=self.request.user
        return Products.objects.exclude(created_by=user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

product_list_create_view=ProductCreateAPIView.as_view()


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes=[IsOwnerOrReadOnly]
    authentication_classes=[TokenAuthentication]


    def get_queryset(self):
        return Products.objects.all()    
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_alter_view=ProductRetrieveUpdateDestroyAPIView.as_view()    


class UserNameAPI(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return Response({'username': user.username})

class ProductNameAPI(APIView):
    def get(self, request, product_id):
        product = Products.objects.get(id=product_id)
        return Response({'product_name': product.name})