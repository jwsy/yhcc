from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('content', 'owner', 'done')
    list_filter = ('content', 'owner', 'done')

# Register your models here.
