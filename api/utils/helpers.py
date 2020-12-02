def has_body_params(request):
    return request.data and request.data != {}


def summarize_serializer_errors(serializer_errors):
    message = ""
    for field in serializer_errors:
        message += f"\nErrors with field >{field}<\n"
        field_errors = serializer_errors[field]
        for error in field_errors:
            message += f">> {error}\n"
    return message
