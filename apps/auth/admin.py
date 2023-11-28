from django.contrib import admin

from apps.auth.models import AuthOtpCode


# Register your models here.


class AuthOtpCodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'otp_code', 'created_at', 'expired_at']
    search_fields = ['user__username', 'user__email', 'otp_code']
    list_filter = ['created_at', 'expired_at']


admin.site.register(AuthOtpCode, AuthOtpCodeAdmin)
