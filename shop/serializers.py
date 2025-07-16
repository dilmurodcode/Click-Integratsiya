from rest_framework import serializers

from shop.models import Order

class OrderSerializer(serializers.ModelSerializer):
    """
    Order model serializer.
    """
    class Meta:
        model = Order
        fields = '__all__'