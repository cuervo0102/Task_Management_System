from django.urls import path
from .views import create_task, index


urlpatterns = [
    path('create-task', create_task, name='create_task'), 
    path('', index, name='index')
]