from django.contrib import admin
from .models import TodoItem, Client, Activity

@admin.register(TodoItem)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'activity', 'done', 'created_at', 'updated_at')
    list_filter = ('client', 'done', 'updated_at')

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # list_display = ('client_id', 'display_name', 'full_name', 'guardian_users')
    list_display = ('id', 'display_name', 'full_name')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'youtube_url')

# class Activities(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.TextField()
#     description = models.TextField(blank=True)
#     youtube_url = models.TextField(blank=True)

#     def __str__(self):
#         return self.namV