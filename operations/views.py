from django.contrib.auth.models import User
from operations.models import *
from operations.serializers import *
from rest_framework import generics
from rest_framework import permissions


class CategoryList(generics.ListCreateAPIView):
    '''
    A view for listing categories and adding new categories.
    '''
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        '''
        Method saving user who created category.
        '''
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    A view for retrieving, editing and deleting categories.
    '''
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer


class CurrencyList(generics.ListCreateAPIView):
    '''
    A view for listing currencies and adding new currencies.
    '''
    queryset = Currency.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CurrencySerializer

    def perform_create(self, serializer):
        '''
        Method saving user who created currency.
        '''
        serializer.save(owner=self.request.user)


class CurrencyDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    A view for retrieving, editing and deleting currencies.
    '''
    queryset = Currency.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CurrencySerializer


class OperationList(generics.ListCreateAPIView):
    '''
    A view for listing operations and adding new operations.
    '''
    queryset = Operation.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = OperationSerializer

    def perform_create(self, serializer):
        '''
        Method saving user who created operation.
        '''
        serializer.save(owner=self.request.user)


class OperationDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    A view for retrieving, editing and deleting operations.
    '''
    queryset = Operation.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = OperationSerializer


class UserList(generics.ListAPIView):
    '''
    A view for listing users.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    '''
    A view for retrieving users.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer