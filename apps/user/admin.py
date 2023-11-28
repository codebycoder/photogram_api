from django.contrib import admin

from apps.user.models import User


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'email', 'birthday', 'is_staff', 'is_active', 'date_joined', 'last_login')
    list_display_links = ('id', 'username', 'name', 'email', 'birthday', 'is_staff', 'is_active', 'date_joined', 'last_login')
    list_filter = ('id', 'username', 'name', 'email', 'birthday', 'is_staff', 'is_active', 'date_joined', 'last_login')
    search_fields = ('id', 'username', 'name', 'email', 'birthday', 'is_staff', 'is_active', 'date_joined', 'last_login')
    list_per_page = 25


admin.site.register(User, UserAdmin)