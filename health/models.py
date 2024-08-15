from django.db import models
from .model_choices import ( 
    INSTITUTION_TYPE, 
    PHONE_TYPES, 
    SERVICE_TYPE_CHOICES,
    POLICY_TITLE_CHOICES,
    LICENSE_TITLE_CHOICES,
    STATUS_CHOICES,
    CERTIFICATION_TITLE_CHOICES
)

class Institution(models.Model):
    institutional_informations = models.OneToOneField('InstitutionalInformation', on_delete=models.PROTECT)
    address = models.OneToOneField('Address', on_delete=models.PROTECT)
    administrative_informations = models.OneToOneField('AdministrativeInformation', on_delete=models.PROTECT)
    policy_informations = models.OneToOneField('PolicyInformation', on_delete=models.PROTECT)
    operation_informations = models.OneToOneField('OperationInformation', on_delete=models.PROTECT)
    licenses = models.OneToOneField('License', on_delete=models.PROTECT)
    certifications = models.OneToOneField('Certification', on_delete=models.PROTECT)

    def __str__(self):
        return self.institutional_information.institution_name

#TODO Consider move some models to management app

class InstitutionalInformation(models.Model):
    institution_name = models.CharField(max_length=150)
    nif = models.CharField(max_length=14)
    institution_type = models.CharField(max_length=3, choices=INSTITUTION_TYPE)
    founding_date = models.DateField()

    def __str__(self):
        return self.institution_name


class Address(models.Model):
    street_address = models.CharField(max_length=120)
    neighborhood = models.CharField(max_length=40)
    province = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=4)

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.street_address


class Phone(models.Model):
    phone_type = models.CharField(max_length=3, choices=PHONE_TYPES)
    number = models.CharField(max_length=9)
    contact_information = models.ForeignKey('ContactInformation', related_name='phone_numbers', on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class ContactInformation(models.Model):
    email = models.EmailField(max_length=150)
    website = models.URLField()

    def __str__(self):
        return self.phone_numbers


class AdministrativeInformation(models.Model):
    responsabile_person_name = models.CharField(max_length=50)
    responsabile_person_nif = models.CharField(max_length=14)
    responsabile_person_email = models.EmailField(max_length=150)
    responsabile_person_phone = models.CharField(max_length=13)


class ServiceType(models.Model):
    service_name = models.CharField(max_length=3, choices=SERVICE_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)


class PolicyInformation(models.Model):
    title = models.CharField(max_length=3, choices=POLICY_TITLE_CHOICES)
    description = models.TextField()
    implementation_date = models.DateField()
    last_review_date = models.DateField(null=True, blank=True)
    document = models.FileField(upload_to='health/documents/policy_documents/', null=True, blank=True)

    def __str__(self):
        return dict(POLICY_TITLE_CHOICES).get(self.title, self.title)


class OperationInformation(models.Model):
    opening_hours = models.TimeField()
    closing_hours = models.TimeField()
    services_offered = models.ManyToManyField(ServiceType, related_name='institutions')


    def __str__(self):
        return f"Open from {self.opening_hours} until {self.closing_hours}"

class License(models.Model):
    license_title = models.CharField(max_length=3, choices=LICENSE_TITLE_CHOICES)
    license_number = models.CharField(max_length=50, unique=True)
    license_status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    issue_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    issuing_authority = models.CharField(max_length=100)
    renewal_required = models.BooleanField(default=True)
    renewal_date = models.DateField(null=True, blank=True)
    scope = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.license_title} - {self.license_number}"


class LicenseDocument(models.Model):
    related_license = models.ForeignKey(License, related_name='documents', on_delete=models.CASCADE)
    file = models.FileField(upload_to='health/documents/license_documents/')
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.license.license_title}"


class Certification(models.Model):
    certification_title = models.CharField(max_length=3, choices=CERTIFICATION_TITLE_CHOICES)
    certification_number = models.CharField(max_length=50, unique=True)
    certification_status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    issue_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    issuing_authority = models.CharField(max_length=100)
    renewal_required = models.BooleanField(default=True)
    renewal_date = models.DateField(null=True, blank=True)
    scope = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.certification_title} - {self.certification_number}"


class CertificationDocument(models.Model):
    related_certification = models.ForeignKey(Certification, related_name='documents', on_delete=models.CASCADE)
    file = models.FileField(upload_to='health/documents/certification_documents/')
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.certification.certification_title}"
