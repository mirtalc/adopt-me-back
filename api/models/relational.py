from api.models import Animal, Vaccine
from django.db import models


class Vaccination(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name="vaccinations")
    vaccine = models.ForeignKey(
        Vaccine, on_delete=models.CASCADE, related_name="vaccinations")
    date_vaccinated = models.DateField()
    incidences = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.animal} | {self.vaccine} | {self.date_vaccinated}"
