from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True)
    youtube_url = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.name
        
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    display_name = models.TextField(blank=True)
    full_name = models.TextField(blank=True)
    guardian_users = models.ManyToManyField(get_user_model(), blank=True)

    def __str__(self):
        return f"{self.id}_{self.display_name}"

class TodoItem(models.Model):
    content = models.TextField(blank=True)
    owner = models.TextField(blank=True)
    
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    # https://stackoverflow.com/questions/3429878/automatic-creation-date-for-django-model-form-objects
    # I had to run a manual `python manage.py makemigrations` and provide a blank date
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # This would be optimal but we can't edit it. So we'll update it in the view
    # updated_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "Activities Attempted"
    
    def __str__(self):
        return str(self.client) + self.content + str(self.updated_at)
    
