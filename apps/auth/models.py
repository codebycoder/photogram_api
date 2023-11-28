from django.db import models


# Create your models here.


class AuthOtpCode(models.Model):
    user = models.ForeignKey('apps_user.User', on_delete=models.CASCADE, related_name='user_otp')
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return self.user

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Auth OTP Code'
        verbose_name_plural = 'Auth OTP Codes'
