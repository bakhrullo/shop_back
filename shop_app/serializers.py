from rest_framework import serializers

from .models import *


class PercentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Percent
        fields = '__all__'


class TgBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgBot
        fields = '__all__'


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = '__all__'


class TgUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = ['user_id']


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
