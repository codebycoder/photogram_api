from rest_framework import serializers

from apps.auth.models import AuthOtpCode


class AuthOTPSerializer(serializers.Serializer):
    grant_type = serializers.CharField(max_length=255, required=True)
    email = serializers.EmailField(required=True)