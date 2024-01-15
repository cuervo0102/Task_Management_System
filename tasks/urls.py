from django.urls import path
from .views import create_task, index, test


urlpatterns = [
    path('create-task/', create_task, name='create_task'), 
    path('test/<int:pk>/', test, name='test'),
    path('', index, name='index_default'),
]