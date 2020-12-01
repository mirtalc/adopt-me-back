from rest_framework.views import exception_handler
from adoptme.handlers.utils import is_custom, is_customizable, error_response


def handler(exception, context):
    if is_custom(exception):
        return handle_custom_exception(exception)
    if is_customizable(exception, context):
        return handle_customizable_exception(exception, context)
    return handle_unknown_exception(exception, context)


def handle_custom_exception(exception):
    return error_response(status=exception.status_code,
                          code=exception.code,
                          message=exception.message)


def handle_customizable_exception(exception, context):
    detail = exception_handler(exception, context).data['detail']
    return error_response(status=exception.status_code,
                          code=detail.code,
                          message=str(detail))


def handle_unknown_exception(exception, context):
    unmodified_response = exception_handler(exception, context)
    return unmodified_response
