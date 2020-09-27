from api.models import TimestampMixin
from django.db import models


class Vaccine(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(null=True, blank=True)
    mandatory = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - mandatory: {self.mandatory}"


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
