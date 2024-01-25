from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Note

admin.site.register(User, UserAdmin)


class NoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Note, NoteAdmin)
