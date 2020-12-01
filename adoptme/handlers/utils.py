from rest_framework.views import exception_handler
from rest_framework.response import Response


def error_response(status, code, message):
    data = {
        'error_code': code,
        'error_message': message
    }
    return Response(data=data, status=status)


def is_custom(exception):
    return hasattr(exception, 'custom')


def is_customizable(exception, context):
    response = exception_handler(exception, context)
    exception_detail = response.data.get('detail', None)
    return exception_detail is not None
