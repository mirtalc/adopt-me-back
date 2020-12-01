from rest_framework.exceptions import APIException, ErrorDetail


class AdoptmeException(APIException):
    custom = True


class ResourceNotFound(AdoptmeException):
    default_status = 404
    default_code = "resource_not_found"
    default_message = "Requested resource was not found in our database"

    def __init__(self,
                 status=default_status,
                 code=default_code,
                 message=default_message):
        self.status_code = status
        self.code = code
        self.message = message
        self.detail = ErrorDetail(code=code, string=message)


class NoValuesSupplied(AdoptmeException):
    default_status = 400
    default_code = "no_values_supplied"
    default_message = "You did not supplied any values to update"

    def __init__(self,
                 status=default_status,
                 code=default_code,
                 message=default_message):
        self.status_code = status
        self.code = code
        self.message = message
        self.detail = ErrorDetail(code=code, string=message)


class InvalidFields(AdoptmeException):
    default_status = 400
    default_code = "invalid_fields"
    default_message = "Invalid value supplied"

    def __init__(self,
                 status=default_status,
                 code=default_code,
                 message=default_message):
        self.status_code = status
        self.code = code
        self.message = message
        self.detail = ErrorDetail(code=code, string=message)
