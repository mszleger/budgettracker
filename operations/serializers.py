from operations.models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'main_category']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'code']

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['name', 'date', 'description', 'category', 'amount', 'currency']