from django.contrib import admin
from .models import Task, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'created', 'updated', 'active')
    list_filter = ('active', 'created', 'updated', 'user')
    search_fields = ('author', 'task', 'user')


admin.site.register(Task)
admin.site.register(Comment, CommentAdmin)