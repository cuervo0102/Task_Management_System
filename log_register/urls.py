from django.urls import path 
from .views import register_request, login_request, test, logout_request, edit_user_profile

urlpatterns = [
    path('', register_request, name='register_request'), 
    path('login/', login_request, name='login_request'),
    path('test/', test, name='test'),
    path('logout/', logout_request, name='logout_request'),
    path('edit-profile/', edit_user_profile, name='edit_user_profile'),
]