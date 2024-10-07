from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderCreationSerializer, OrderDetailSerializer
from .models import Order
from rest_framework.permissions import IsAuthenticated

class HelloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Welcome to the Order API"}, status=status.HTTP_200_OK)

class OrderCreationListView(generics.GenericAPIView):
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()  # No customer data to save
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(generics.GenericAPIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        serializer = OrderDetailSerializer(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        data = request.data
        order = Order.objects.get(id=order_id)
        serializer = OrderDetailSerializer(instance=order, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order.delete()
        return Response(data={"message": "Order deleted successfully"}, status=status.HTTP_200_OK)
