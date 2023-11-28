from django.contrib import admin

from apps.profile.models import UserProfile


# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_update', 'created_at',)


admin.site.register(UserProfile, ProfileAdmin)
