from rest_framework import generics,permissions
from .models import Products
from .serializers import ProductSerializer
from rest_framework import viewsets

class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer

product_list_create_view=ProductCreateAPIView.as_view()

# Create your views here.
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Products.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Products.objects.all()

product_alter_view=ProductRetrieveUpdateDestroyAPIView.as_view()    