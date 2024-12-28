from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('currencies/', views.CurrencyList.as_view()),
    path('currencies/<int:pk>/', views.CurrencyDetail.as_view()),
    path('operations/', views.OperationList.as_view()),
    path('operations/<int:pk>/', views.OperationDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)