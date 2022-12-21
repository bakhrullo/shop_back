from rest_framework import serializers

from .models import *


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class TgAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgAdmin
        fields = '__all__'
