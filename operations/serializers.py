from operations.models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CategoryGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryGroup
        fields = ['main_category', 'sub_category']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'code']

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['name', 'date', 'description', 'category', 'amount', 'currency']