from django import forms
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
    License,
    Address,
    Phone
)


class InstitutionalInformationForm(forms.ModelForm):
    class Meta:
        model = InstitutionalInformation
        fields = '__all__'
        widgets = {
            'institution_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'nif': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'institution_type': forms.Select(attrs={'class': 'form-control mb-3'}),
            'founding_date': forms.DateInput(attrs={'class': 'form-control mb-3'})
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        widgets = {
            'street_address': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'province': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control mb-3'})
        }
       

class AdministrativeInformationForm(forms.ModelForm):
    class Meta:
        model = AdministrativeInformation
        fields = '__all__'
        widgets = {
            'responsabile_person_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'responsabile_person_nif': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'responsabile_person_email': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'responsabile_person_phone': forms.TextInput(attrs={'class': 'form-control mb-3'})
        }



class CertificationDocumentForm(forms.ModelForm):
    class Meta:
        model = CertificationDocument
        fields = ['file', 'description']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'})
        }


class OperationInformationForm(forms.ModelForm):
    class Meta:
        model = OperationInformation
        fields = ['opening_hours', 'closing_hours']
        widgets = {
            'opening_hours': forms.TimeInput(attrs={'class': 'form-control mb-3'}),
            'closing_hours': forms.TimeInput(attrs={'class': 'form-control mb-3'}),
        }
