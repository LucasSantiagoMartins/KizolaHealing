from django.contrib import admin
from .models import (
    AdministrativeInformation,
    InstitutionalInformation, 
    CertificationDocument,
    OperationInformation,
    ContactInformation,
    PolicyInformation,
    LicenseDocument,
    Certification,
    Institution,
    ServiceType,
    License,
    Address,
    Phone
)


admin.site.register(AdministrativeInformation)
admin.site.register(InstitutionalInformation)
admin.site.register(CertificationDocument)
admin.site.register(OperationInformation)
admin.site.register(ContactInformation)
admin.site.register(PolicyInformation)
admin.site.register(LicenseDocument)
admin.site.register(Certification)
admin.site.register(ServiceType)
admin.site.register(Institution)
admin.site.register(Address)
admin.site.register(License)
admin.site.register(Phone)