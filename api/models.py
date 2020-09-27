from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Animal(TimestampMixin):
    # Establish options for status
    PROCESSING = 'PROC'
    AVAILABLE = 'AVAIL'
    ADOPTED = 'ADOP'
    TRANSFERRED = 'TRANS'
    DECEASED = 'RIP'

    STATUS_CHOICES = (
        (PROCESSING, 'Processing or recovering; cannot yet be adopted'),
        (AVAILABLE, 'Available for adopting'),
        (ADOPTED, 'Already adopted. Yay!'),
        (TRANSFERRED, 'Transferred to another shelter'),
        (DECEASED, 'Unfortunately, it is deceased')
    )

    name = models.CharField(max_length=50, default='Mistery')
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default=PROCESSING)

    def __str__(self):
        return f"{self.name} ({self.status}) - registered at {self.created_at}"


class Vaccine(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(null=True, blank=True)
    mandatory = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - mandatory: {self.mandatory}"


class Vaccination(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name="vaccinations")
    vaccine = models.ForeignKey(
        Vaccine, on_delete=models.CASCADE, related_name="vaccinations")
    date_vaccinated = models.DateField()
    incidences = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.animal} | {self.vaccine} | {self.date_vaccinated}"
