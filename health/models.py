from django.db import models
from .model_choices import ( 
    INSTITUTION_TYPE, 
    PHONE_TYPES, 
    SERVICE_TYPE_CHOICES,
    POLICY_TITLE_CHOICES
)


class InstitutionalInformation(models.Model):
    institution_name = models.CharField(max_length=150)
    nif = models.CharField(max_length=14)
    institution_type = models.CharField(max_length=3, choices=INSTITUTION_TYPE)

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