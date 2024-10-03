from rest_framework import serializers


from .models import Order

class OrderCreationSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(max_length=20)
    size = serializers.CharField(max_length=20)
    quantity = serializers.CharField()
    order_status = serializers.CharField(max_length=20, default="PENDING")
    
    class Meta:
        model = Order
        fields = ['food_name', 'size', 'quantity', 'order_status']

    def create(self, validated_data):
        # The customer will be added in the view
        return Order.objects.create(**validated_data)

class OrderDetailSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(max_length=20)
    size = serializers.CharField(max_length=20)
    quantity = serializers.CharField()
    order_status = serializers.CharField(max_length=20,default="PENDING")
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Order
        fields = ['food_name','size','quantity','order_status','created_at','updated_at']
