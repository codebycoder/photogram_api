
from rest_framework.response import Response


class CustomApiError(Exception):

    def __init__(self, status_code: int, message: str, code: str, details: any = None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.message = message
        self.code = code
        self.details = details

    def get_response(self):

        if self.details is None:
            return Response(data={
                'message': self.message,
                'code': self.code,
            }, status=self.status_code)
        else:
            return Response(data={
                'message': self.message,
                'code': self.code,
                'details': self.details
            }, status=self.status_code)
