from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class SendAuthOtpAPI(APIView):
    permission_classes = []
    serializer_class = SendAuthOtpSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            try:
                user = User.objects.get(phone_number=phone_number)
            except User.DoesNotExist:
                return Response({'status': 'error', 'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
            otp = randint(100000, 999999)
            user.otp = otp
            user.save()
            send_otp(phone_number, otp)
            return Response({'status': 'success', 'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': 'Invalid phone number'}, status=status.HTTP_400_BAD_REQUEST