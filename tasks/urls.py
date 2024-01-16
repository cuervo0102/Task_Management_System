from django.urls import path
from .views import create_task, index, task_details


urlpatterns = [
    path('create-task/', create_task, name='create_task'), 
    path('', index, name='index_default'),
    path('detail/<int:pk>',task_details, name='detail')
]