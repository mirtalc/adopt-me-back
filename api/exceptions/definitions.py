from rest_framework.exceptions import APIException, ErrorDetail


class ResourceNotFound(APIException):
    def __init__(self,
                 status=404,
                 code='resource_not_found',
                 message="Requested resource was not found in our database"
                 ):
        self.status_code = status
        self.detail = ErrorDetail(code=code, string=message)


class NoValuesSupplied(APIException):
    def __init__(self,
                 status=400,
                 code='no_values_supplied',
                 message="You did not supplied any values to update"
                 ):
        self.status_code = status
        self.detail = ErrorDetail(code=code, string=message)


class InvalidFields(APIException):
    def __init__(self,
                 status=400,
                 code='invalid_fields',
                 message='Invalid value supplied'
                 ):
        self.status_code = status
        self.detail = ErrorDetail(code=code, string=message)
