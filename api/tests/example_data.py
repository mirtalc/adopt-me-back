from api.models import Animal, Vaccine


def create_mock_animals():
    get_mock_animal(1, 'Sudo', 'ADOP')
    get_mock_animal(2, 'Laika', 'RIP')


def create_mock_vaccines():
    get_mock_vaccine(1, 'Bordetella Bronchiseptica',
                        'This highly infectious bacterium causes severe fits of coughing, whooping, vomiting, and, in rare cases, seizures and death. It is the primary cause of kennel cough.',
                        mandatory=True),
    get_mock_vaccine(2, 'Canine Distemper',
                        'A severe and contagious disease caused by a virus that attacks the respiratory, gastrointestinal (GI), and nervous systems of dogs.',
                        mandatory=False),
    get_mock_vaccine(3, 'Canine Hepatitis',
                        'Infectious canine hepatitis is a highly contagious viral infection that affects the liver, kidneys, spleen, lungs, and the eyes of the affected dog.',
                        mandatory=False),


def get_mock_animal(animal_id, name, status, vaccinations=[]):
    animal, animal_created = Animal.objects.get_or_create(pk=animal_id)
    animal.name = name
    animal.status = status
    animal.vaccinations.set(vaccinations)
    animal.save()

    return animal


def get_mock_vaccine(vaccine_id, name, description='', mandatory=False):
    vaccine, vaccine_created = Vaccine.objects.get_or_create(pk=vaccine_id)
    vaccine.name = name
    vaccine.description = description
    vaccine.mandatory = mandatory
    vaccine.save()

    return vaccine
