from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    task_writer = models.ForeignKey(User, models.CASCADE, related_name='tasks_written', default=1)
    processors = models.ManyToManyField(User, related_name='tasks_processed')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    # status = models.CharField(choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20)
    priority = models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')], max_length=10)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} - {self.priority}'