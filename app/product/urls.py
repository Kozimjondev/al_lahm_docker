from django.urls import path
from .views import *


urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('accessory/', AccessoryListCreateAPIView.as_view(), name='accessory'),
    path('accessory/<int:pk>/', AccessoryDetailAPIView.as_view(), name='accessory-detail'),
    path('review/', ReviewListCreateAPIView.as_view(), name='review'),
    path('connection/', ConnectionPostView.as_view(), name='connection'),
    path('login/', login, name='login'),
    path('connection-list/', ConnectionListAPIView.as_view(), name='connection-list')
]
