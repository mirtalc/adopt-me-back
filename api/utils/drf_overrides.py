from rest_framework.views import exception_handler


def custom_exception_handler(exception, context):
    response = exception_handler(exception, context)

    if response is not None:
        response.data['error_code'] = 'unknown'
        if response.data.get('detail', None):
            response.data['error_code'] = response.data['detail'].code
            response.data.pop('detail')
        response.data['error_message'] = str(exception)
        # //TODO review exception treatment with different formats, such as raised by JWT
    return response
