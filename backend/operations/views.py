from django.contrib.auth.models import User
from operations.models import *
from operations.serializers import *
from rest_framework import generics
from rest_framework import permissions


class CategoryList(generics.ListCreateAPIView):
    '''
    A view for listing categories and adding new categories.
    '''
    queryset = None
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        '''
        Method saving user who created category.
        '''
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        '''
        Override the queryset to return only categories created by the current user.
        '''
        return Category.objects.filter(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    A view for retrieving, editing and deleting categories.
    '''
    queryset = None
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self):
        '''
        Override the queryset to return only categories created by the current user.
        '''
        return Category.objects.filter(owner=self.request.user)


class CurrencyList(generics.ListCreateAPIView):
    '''
    A view for listing currencies and adding new currencies.
    '''
    queryset = None
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CurrencySerializer

    def perform_create(self, serializer):
        '''
        Method saving user who created currency.
        '''
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        '''
        Override the queryset to return only currencies created by the current user.
        '''
        return Currency.objects.filter(owner=self.request.user)


class CurrencyDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    A view for retrieving, editing and deleting currencies.
    '''
    queryset = None
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CurrencySerializer

    def get_queryset(self):
        '''
        Override the queryset to return only currencies created by the current user.
        '''
        return Currency.objects.filter(owner=self.request.user)


class OperationList(generics.ListCreateAPIView):
    '''
    A view for listing operations and adding new operations.
    '''
    queryset = None
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OperationSerializer

    def perform_create(self, serializer):
        '''
        Method saving user who created operation.
        '''
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        '''
        Override the queryset to return only operations created by the current user.
        '''
        return Operation.objects.filter(owner=self.request.user)


class OperationDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    A view for retrieving, editing and deleting operations.
    '''
    queryset = None
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OperationSerializer

    def get_queryset(self):
        '''
        Override the queryset to return only operations created by the current user.
        '''
        return Operation.objects.filter(owner=self.request.user)


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