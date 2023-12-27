from django.urls import path 
from .views import register_request, login_request

urlpatterns = [
    path('', register_request, name='register_request'), 
    path('login/', login_request, name='login_request')
]