from django.db import models
from .model_choices import INSTITUTION_TYPE, PHONE_TYPES


class BasicInformation(models.Model):
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
    phone_type = models.CharField(max_legth=3, choices=PHONE_TYPES)
    number = models.CharField(max_length=9)
    