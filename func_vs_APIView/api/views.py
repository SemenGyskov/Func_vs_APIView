from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .models import *
from .serializers import *
from rest_framework.generics import *

class ProductViewSet(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'data':serializer.data}, status=status.HTTP_200_OK)
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'product_id':serializer.data['id'],
                'message': 'Product was added'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class ProductUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response({'error':{'code':404,'message':'Not found'}})
        serializer = ProductSerializer(product, many=False)
        return Response({'data':serializer.data}, status= HTTP_200_OK)
    def put(self,request,*args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response({'error':{'code':404,'message':'Not found'}})
        serializers = ProductSerializer(data=request.data, instance=product)
        if serializers.is_valid():
            serializers.save()
            return Response({'data':serializers.data}, status = HTTP_200_OK)
        return Response(serializers.errors)
    def patch(self,request,*args,**kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response({'errors':{'code':404, 'message':'Not Found'}})
        serializers = ProductSerializer(product, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'data':serializers.data}, status = HTTP_200_OK)
        return Response(serializers.errors)
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({'data':{'message':'Product deleted'}})

class CartViewSet(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'cart_id': serializer.data['id'],
                'message': 'cart was added'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class CartUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        try:
            cart = Cart.objects.get(pk=pk)
        except:
            return Response({'error':{'code':404,'message':'Not found'}})
        serializer = CartSerializer(cart, many=False)
        return Response({'data':serializer.data}, status= HTTP_200_OK)
    def put(self,request,*args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        try:
            cart = Cart.objects.get(pk=pk)
        except:
            return Response({'error':{'code':404,'message':'Not found'}})
        serializers = CartSerializer(data=request.data, instance=cart)
        if serializers.is_valid():
            serializers.save()
            return Response({'data':serializers.data}, status = HTTP_200_OK)
        return Response(serializers.errors)
    def patch(self,request,*args,**kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        try:
            cart = Cart.objects.get(pk=pk)
        except:
            return Response({'errors':{'code':404, 'message':'Not Found'}})
        serializers = CartSerializer(cart, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'data':serializers.data}, status = HTTP_200_OK)
        return Response(serializers.errors)
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        cart = Cart.objects.get(pk=pk)
        cart.delete()
        return Response({'data':{'message':'Cart deleted'}})


class OrderViewSet(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'cart_id': serializer.data['id'],
                'message': 'cart was added'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class OrderUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        try:
            order = Order.objects.get(pk=pk)
        except:
            return Response({'error':{'code':404,'message':'Not found'}})
        serializer = OrderSerializer(order, many=False)
        return Response({'data':serializer.data}, status= HTTP_200_OK)
    def put(self,request,*args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        try:
            order = Order.objects.get(pk=pk)
        except:
            return Response({'error':{'code':404,'message':'Not found'}})
        serializers = OrderSerializer(data=request.data, instance=order)
        if serializers.is_valid():
            serializers.save()
            return Response({'data':serializers.data}, status = HTTP_200_OK)
        return Response(serializers.errors)
    def patch(self,request,*args,**kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        try:
            order = Order.objects.get(pk=pk)
        except:
            return Response({'errors':{'code':404, 'message':'Not Found'}})
        serializers = OrderSerializer(order, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'data':serializers.data}, status = HTTP_200_OK)
        return Response(serializers.errors)
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error':'Method PUT not allowed'})
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response({'data':{'message':'Order deleted'}})