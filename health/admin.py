from django.contrib import admin
from .models import (
    InstitutionalInformation, 
    Address,
    Institution,
    Phone,
    AdministrativeInformation,
    Certification,
    License,
    CertificationDocument,
    LicenseDocument,
    ContactInformation,
    OperationInformation,
    PolicyInformation
)

admin.site.register(InstitutionalInformation)
admin.site.register(AdministrativeInformation)
admin.site.register(CertificationDocument)
admin.site.register(OperationInformation)
admin.site.register(ContactInformation)
admin.site.register(PolicyInformation)
admin.siter.register(LicenseDocument)
admin.site.register(Certification)
admin.site.register(Institution)
admin.site.register(Address)
admin.site.register(License)
admin.site.register(Phone)