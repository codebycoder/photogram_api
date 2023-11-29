

from rest_framework import status

SERVER_METHODE_NOT_ALLOWED = {
    'status_code': status.HTTP_405_METHOD_NOT_ALLOWED,
    'message': 'Method not allowed',
    'code': 'core:method-not-allowed',
}

SERVER_NOT_FOUND = {
    'status_code': status.HTTP_404_NOT_FOUND,
    'message': 'Not found',
    'code': 'core:not-found',
}

SERVER_BAD_REQUEST = {
    'status_code': status.HTTP_400_BAD_REQUEST,
    'message': 'Bad request',
    'code': 'core:bad-request',
}

SERVER_INTERNAL_ERROR = {
    'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
    'message': 'Internal server error',
    'code': 'core:internal-server-error',
}

SERVER_NOT_ACCEPTABLE = {
    'status_code': status.HTTP_406_NOT_ACCEPTABLE,
    'message': 'Not acceptable',
    'code': 'core:not-acceptable',
}


INVALID_API_KEY = {

    'status_code': status.HTTP_403_FORBIDDEN,
    'message': 'Invalid API key',
    'code': 'core:invalid-api-key',
}
