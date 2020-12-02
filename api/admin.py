from django.contrib import admin
from api.models import Animal, Vaccine, Vaccination, Species, AdoptionStatus

admin.site.register(Animal)
admin.site.register(Vaccine)
admin.site.register(Vaccination)
admin.site.register(Species)
admin.site.register(AdoptionStatus)
