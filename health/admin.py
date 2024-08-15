from django.contrib import admin
from .models import (
    InstitutionalInformation, 
    Address,
    Institution,
    Phone,
    AdministrativeInformation,
    Certification
)

admin.site.register(InstitutionalInformation)
admin.site.register(AdministrativeInformation)
admin.site.register(Certification)
admin.site.register(Institution)
admin.site.register(Address)
admin.site.register(Phone)