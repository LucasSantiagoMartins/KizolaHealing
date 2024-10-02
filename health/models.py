from django.db import models
from .model_choices import ( 
    INSTITUTION_TYPE, 
    PHONE_TYPES, 
    SERVICE_TYPE_CHOICES,
    POLICY_TITLE_CHOICES,
    LICENSE_TITLE_CHOICES,
    STATUS_CHOICES,
    CERTIFICATION_TITLE_CHOICES,
    SHIFT_TYPE_CHOICES,
    HOURS_CHOICES,
    WEEK_DAYS_CHOICES,
    OPERATING_HOURS_CHOICES
)
from .utils import get_readable_form_of_choice
from . import model_validators

class Institution(models.Model):
    institutional_informations = models.OneToOneField('InstitutionalInformation', on_delete=models.PROTECT)
    address = models.OneToOneField('Address', on_delete=models.PROTECT)
    administrative_informations = models.OneToOneField('AdministrativeInformation', on_delete=models.PROTECT)
    operation_informations = models.OneToOneField('OperationInformation', on_delete=models.PROTECT)
    # related_name='policy_informations'
    # related_name='licenses'
    # related_name='certifications'

    def __str__(self):
        return self.institutional_informations.institution_name

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
    related_institution = models.OneToOneField(Institution, related_name='contact_informations', on_delete=models.DO_NOTHING)
    # related_name='phone_numbers' from Phone model

    def __str__(self):
        return self.phone_numbers


class AdministrativeInformation(models.Model):
    responsible_person_name = models.CharField(max_length=50)
    responsible_person_nif = models.CharField(max_length=14)
    responsible_person_email = models.EmailField(max_length=150)
    responsible_person_phone = models.CharField(max_length=13, validators=[model_validators.phone_number_validator])

    def __str__(self):
        return self.responsible_person_name

class ServiceOffered(models.Model):
    service_name = models.CharField(max_length=3, choices=SERVICE_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.service_name

class PolicyInformation(models.Model):
    title = models.CharField(max_length=3, choices=POLICY_TITLE_CHOICES)
    description = models.TextField()
    implementation_date = models.DateField()
    last_review_date = models.DateField(null=True, blank=True)
    document = models.FileField(upload_to='health/documents/policy_documents/', null=True, blank=True)
    institution = models.ForeignKey(Institution, related_name='policy_informations', on_delete=models.DO_NOTHING)

    def __str__(self):
        return dict(POLICY_TITLE_CHOICES).get(self.title, self.title)


class OperationInformation(models.Model):
    services_offered = models.ManyToManyField(ServiceOffered)
    # related_name='operating_shifts' from OperatingShift model
    # related_name='duty_shifts' from DutyShift model
    # related_name='operating_hours', from OperatingHour model

    def __str__(self):
        return self.services_offered.all()

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
    institution = models.ForeignKey(Institution, related_name='licenses', on_delete=models.DO_NOTHING)

    # related_name='documents' from LicenseDocument model

    def __str__(self):
        return f"{self.license_title} - {self.license_number}"


class LicenseDocument(models.Model):
    related_license = models.ForeignKey(License, related_name='documents', on_delete=models.CASCADE)
    file = models.FileField(upload_to='health/documents/license_documents/')
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.file.name}"


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
    # related_name='documents' from CertificationDocument model
    institution = models.ForeignKey(Institution, related_name='certifications', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.certification_title} - {self.certification_number}"


class CertificationDocument(models.Model):
    related_certification = models.ForeignKey(Certification, related_name='documents', on_delete=models.CASCADE)
    file = models.FileField(upload_to='health/documents/certification_documents/')
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.related_certification.certification_title}"

class OperatingShift(models.Model):
    shift_type = models.CharField(max_length=3, choices=SHIFT_TYPE_CHOICES)
    begin_hour = models.CharField(max_length=3, choices=HOURS_CHOICES)
    end_hour = models.CharField(max_length=3, choices=HOURS_CHOICES)
    operation_information = models.ForeignKey(OperationInformation, related_name='operating_shifts', on_delete=models.CASCADE)

    @property
    def duration(self):
        readable_form_hours = {
            'begin_hour': get_readable_form_of_choice(HOURS_CHOICES, self.begin_hour),
            'end_hour': get_readable_form_of_choice(HOURS_CHOICES, self.end_hour)
        }
         
        return f"Das {readable_form_hours['begin_hour']} às {readable_form_hours['end_hour']}."

    def __str__(self):
        return self.shift_type


class DutyShift(models.Model):
    name = models.CharField(max_length=30)
    operating_shift = models.ForeignKey(OperatingShift, on_delete=models.DO_NOTHING)
    description = models.TextField()
    begin_day = models.CharField(max_length=2, choices=WEEK_DAYS_CHOICES)
    end_day = models.CharField(max_length=2, choices=WEEK_DAYS_CHOICES)
    operation_information = models.ForeignKey(OperationInformation, related_name='duty_shifts', on_delete=models.CASCADE)


    def __str__(self):
        readable_form_days = {
            'begin_day': get_readable_form_of_choice(WEEK_DAYS_CHOICES, self.begin_day),
            'end_day': get_readable_form_of_choice(WEEK_DAYS_CHOICES, self.end_day)
        }

        return f"{readable_form_days['begin_day']} à {readable_form_days['end_day']}: {self.operating_shift.duration}"

class OperatingHour(models.Model):
    operating_hour = models.CharField(max_length=3, choices=OPERATING_HOURS_CHOICES)
    begin_day = models.CharField(max_length=2, choices=WEEK_DAYS_CHOICES)
    end_day = models.CharField(max_length=2, choices=WEEK_DAYS_CHOICES)
    begin_hour = models.CharField(max_length=3, choices=HOURS_CHOICES)
    end_hour = models.CharField(max_length=3, choices=HOURS_CHOICES)
    operation_information = models.ForeignKey(OperationInformation, related_name='operating_hours', on_delete=models.CASCADE)

    def __str__(self):
        readable_form_days_and_hours = {
            'begin_day': get_readable_form_of_choice(WEEK_DAYS_CHOICES, self.begin_day),
            'end_day': get_readable_form_of_choice(WEEK_DAYS_CHOICES, self.end_day),
            'begin_hour': get_readable_form_of_choice(HOURS_CHOICES, self.begin_hour),
            'end_hour': get_readable_form_of_choice(HOURS_CHOICES, self.end_hour)
        }

        return f"{readable_form_days_and_hours['begin_day']} à {readable_form_days_and_hours['end_day']}: {readable_form_days_and_hours['begin_hour']} às {readable_form_days_and_hours['end_hour']}."