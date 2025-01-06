from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('task', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed',)
    search_fields = ('task',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('id', 'task', 'completed')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    actions = ['mark_as_completed', 'mark_as_incomplete']

    def mark_as_completed(self, request, queryset):
        queryset.update(completed=True)
    mark_as_completed.short_description = "Mark selected todos as completed"

    def mark_as_incomplete(self, request, queryset):
        queryset.update(completed=False)
    mark_as_incomplete.short_description = "Mark selected todos as incomplete"