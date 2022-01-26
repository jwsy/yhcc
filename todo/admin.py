from django.contrib import admin
from .models import TodoItem, Client, Activity, RandomGiphy
from .forms import ActivityForm

@admin.register(TodoItem)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'activity', 'done', 'updated_at')
    list_filter = ('client', 'done', 'updated_at')

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # list_display = ('client_id', 'display_name', 'full_name', 'guardian_users')
    list_display = ('id', 'display_name', 'full_name')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    form = ActivityForm
    list_display = ('name', 'description', 'youtube_url', 'color')

@admin.register(RandomGiphy)
class RandomGiphyAdmin(admin.ModelAdmin):
    list_display = ('description', 'url')
