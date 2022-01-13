from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    owner = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    # https://stackoverflow.com/questions/3429878/automatic-creation-date-for-django-model-form-objects
    # I had to run a manual `python manage.py makemigrations` and provide a blank date
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)