from rest_framework.settings import api_settings
from rest_framework.parsers import FileUploadParser


def all_parser_classes():
    parser_classes = api_settings.DEFAULT_PARSER_CLASSES
    parser_classes.append(FileUploadParser)

    return parser_classes


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
