from django.contrib import admin
from todo_list.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)
