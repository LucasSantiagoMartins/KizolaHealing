from django.contrib import admin
from .models import (
    InstitutionalInformation, 
    Address,
    Institution,
    Phone,
    AdministrativeInformation
)

admin.site.register(InstitutionalInformation)
admin.site.register(Institution)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(AdministrativeInformation)
 