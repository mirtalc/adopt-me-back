from rest_framework.exceptions import ParseError
from api.exceptions.definitions import ResourceNotFound, NoValuesSupplied, InvalidFields


def animal_not_found(animal_id):
    message = f"Animal with id {animal_id} was not found in our database"
    raise ResourceNotFound(message=message)


def vaccine_not_found(vaccine_id):
    message = f"Vaccine with id {vaccine_id} was not found in our database"
    raise ResourceNotFound(message=message)


def no_values_supplied():
    raise NoValuesSupplied()


def invalid_fields(field_errors):
    message = f"Invalid field values found: {field_errors}"
    raise InvalidFields(message=message)


def attached_file_missing():
    message = "Attachment file missing required for this action"
    raise ParseError(message)
