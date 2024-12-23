from django.urls import path, include

urlpatterns = [
    path('', include('operations.urls')),
    path('api-auth/', include('rest_framework.urls')),
]