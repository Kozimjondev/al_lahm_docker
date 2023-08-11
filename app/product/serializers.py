from rest_framework import serializers
from .models import Product, Accessory, Review, Connection


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'amount', 'image')


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = ('name', 'price', 'number', 'image')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('full_name', 'mark', 'description', )


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ("full_name", 'phone_number', 'message')
