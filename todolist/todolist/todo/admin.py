from django.contrib import admin

# Register your models here.
from .models import Todo
class TodoAdmin(admin.ModelAdmin):
	class Meta:
		model = Todo

admin.site.register(Todo, TodoAdmin)