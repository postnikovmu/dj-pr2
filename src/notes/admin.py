from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Note

admin.site.register(User, UserAdmin)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    fields = ["text", "user"]
    list_display = ["pk", "text", "user"]
