from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoAdmin(admin.ModelAdmin):
     list_display = ('content', 'owner')
     list_filter = ('content', 'owner')

# admin.site.register(TodoItem)

# Register your models here.
