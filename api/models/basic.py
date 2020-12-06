from django.db import models
from api.models import TimestampMixin


class Vaccine(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(null=True, blank=True)
    mandatory = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - mandatory: {self.mandatory}"


class Animal(TimestampMixin):
    name = models.CharField(max_length=50, default='Mistery')
    species = models.ForeignKey(
        'Species', on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(
        'AdoptionStatus', on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='pets', null=True)

    def __str__(self):
        return f"{self.name} | {self.species.name } | {self.status.name }"


class Species(models.Model):
    uid = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    fullname = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Species"

    def __str__(self):
        return f"{self.uid} ({self.name}) {self.fullname}"


class AdoptionStatus(models.Model):
    uid = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Adoption statuses"

    def __str__(self):
        return f"{self.uid} ({self.name})"
