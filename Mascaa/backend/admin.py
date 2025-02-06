from django.contrib import admin

# Register your models here.
from .models import User
from .models import lib_Admin

@admin.register(User)
class BookAdmin(admin.ModelAdmin):
    list_display = ('username', 'password','Name','profile_photo','DOB','Branch','Roll_no','Address')
    search_fields = ('Roll_no','Name')

@admin.register(lib_Admin)
class BookAdmin(admin.ModelAdmin):
    list_display = ('username', 'password','Name','DOB','POR','lib_Admin_no','Address')
    search_fields = ('lib_Admin_no','Name','POR')