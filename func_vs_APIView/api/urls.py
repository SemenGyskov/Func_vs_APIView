from django.urls import path, include
from .views import *
urlpatterns = [
    path('products/', ProductViewSet.as_view()),
    path('products/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('cart/', CartViewSet.as_view()),
    path('cart/<int:pk>/', CartUpdateAPIView.as_view()),
    path('order/', OrderViewSet.as_view()),
    path('order/<int:pk>/', OrderUpdateAPIView.as_view()),
    path('', include('rest_framework.urls')),
]
