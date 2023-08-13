from django.urls import path,include
from .import views


urlpatterns=[    
    path('product/',views.product_list_create_view,name='product-list'),
    path('product/<int:pk>/',views.product_alter_view,name='product-alter'),
]