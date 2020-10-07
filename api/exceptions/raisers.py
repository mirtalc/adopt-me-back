from api.exceptions.definitions import ResourceNotFound


def animal_not_found(animal_id):
    message = f"Animal with id {animal_id} was not found in our database"
    raise ResourceNotFound(message=message)
