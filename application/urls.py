from django.urls import path,include
from .import views


urlpatterns=[    
    path('product/',views.product_list_create_view,name='product-list'),
    path('product/<int:pk>/',views.product_alter_view,name='product-alter'),
    path('product/name/<int:pk>/',views.ProductNameAPI.as_view,name='product-name'),
    path('user/name/<int:pk>/',views.UserNameAPI.as_view,name='user-name'),
]