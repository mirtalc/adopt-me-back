from rest_framework.views import exception_handler


def custom_exception_handler(exception, context):
    response = exception_handler(exception, context)

    if response is not None:
        response.data['error_code'] = response.data['detail'].code
        response.data['error_message'] = str(exception)
        response.data.pop('detail')

    return response
