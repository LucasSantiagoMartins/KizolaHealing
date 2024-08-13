from django.db import models
from .models_choices import INSTITUTION_TYPE


class BasicInformation(models.Model):
    institution_name = models.CharField(max_length=150)
    nif = models.CharField(max_length=14)
    institution_type = models.CharField(max_length=3, choices=INSTITUTION_TYPE)


class Address(models.Model):
    street_address = models.CharField(max_length=120)
    neighborhood = models.CharField(max_length=40)
    province = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=4)

    class Meta:
        verbose_name_plural = 'Addresses'
