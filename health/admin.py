from django.contrib import admin
from .models import (
    InstitutionalInformation, 
    Address,
    Institution
)

admin.site.register(InstitutionalInformation)
admin.site.register(Institution)
admin.site.register(Address)

 