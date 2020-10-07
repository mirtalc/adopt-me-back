from rest_framework.exceptions import APIException, ErrorDetail


class ResourceNotFound(APIException):
    def __init__(self,
                 status=404,
                 code='resource_not_found',
                 message="Requested resource was not found in our database"
                 ):
        self.status_code = status
        self.detail = ErrorDetail(code=code, string=message)
