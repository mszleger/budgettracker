from django.contrib.auth.models import User
from api.models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    operations = serializers.PrimaryKeyRelatedField(many=True, queryset=Operation.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = ['name', 'operations', 'main_category', 'sub_categories', 'owner']


class CurrencySerializer(serializers.ModelSerializer):
    operations = serializers.PrimaryKeyRelatedField(many=True, queryset=Operation.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Currency
        fields = ['name', 'code', 'operations', 'owner']


class OperationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Operation
        fields = ['name', 'date', 'description', 'category', 'amount', 'currency', 'owner']


class UserSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    currencies = serializers.PrimaryKeyRelatedField(many=True, queryset=Currency.objects.all())
    operations = serializers.PrimaryKeyRelatedField(many=True, queryset=Operation.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'categories', 'currencies', 'operations']