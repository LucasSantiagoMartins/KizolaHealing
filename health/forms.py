from django import forms
from .models import (
    AdministrativeInformation,
    InstitutionalInformation, 
    CertificationDocument,
    ContactInformation,
    PolicyInformation,
    LicenseDocument,
    Certification,
    OperatingHour,
    ServiceType,
    DutyShift,
    License,
    Address,
    Phone,
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
            'responsible_person_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'responsible_person_nif': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'responsible_person_email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'responsible_person_phone': forms.NumberInput(attrs={'class': 'form-control mb-3'})
        }



class CertificationDocumentForm(forms.ModelForm):
    class Meta:
        model = CertificationDocument
        fields = ['file', 'description']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'})
        }


class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'website': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }


class PolicyInformationForm(forms.ModelForm):
    class Meta:
        model = PolicyInformation
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'implementation_date': forms.DateInput(attrs={'class': 'form-control mb-3'}),
            'last_review_date': forms.DateInput(attrs={'class': 'form-control mb-3'}),
            'document': forms.FileInput(attrs={'class': 'form-control mb-3'})
        }


class LicenseDocumentForm(forms.ModelForm):
    class Meta:
        model = LicenseDocument
        fields = ['file', 'description']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'})
        }


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'
        widgets = {
            'certification_title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'certification_number': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'certification_status': forms.Select(attrs={'class': 'form-control mb-3'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control mb-3'}),
            'issuing_authority': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'renewal_required': forms.CheckboxInput(attrs={'class': 'form-control mb-3'}),
            'renewal_date': forms.DateInput(attrs={'class': 'form-control mb-3'}),
            'scope': forms.TextInput(attrs={'class': 'form-control mb-3'})  
        }
        


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = '__all__'
        widgets = {
            'license_title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'license_number': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'license_status': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control mb-3'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control mb-3'}),
            'issuing_authority': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'renewal_required': forms.CheckboxInput(attrs={'class': 'form-control mb-3'}),
            'renewal_date': forms.DateInput(attrs={'class': 'form-control mb-3'}),
            'scope': forms.TextInput(attrs={'class': 'form-control mb-3'})
        }



class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['phone_type', 'number']
        widgets = {
            'phone_type': forms.Select(attrs={'class': 'form-control mb-3'}),
            'number': forms.NumberInput(attrs={'class': 'form-control mb-3'})
        }

class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = ServiceType
        fields = '__all__'
        widgets = {
            'service_name': forms.Select(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'})
        }

class OperatingHourForm(forms.ModelForm):
    class Meta:
        model = OperatingHour
        fields = ['operating_hour', 'begin_day', 'end_day', 'begin_hour', 'end_hour']
        widgets = {
            'operating_hour': forms.Select(attrs={'class': 'form-control mb-3'}),
            'begin_day': forms.Select(attrs={'class': 'form-control mb-3'}),
            'end_day': forms.Select(attrs={'class': 'form-control mb-3'}),
            'begin_hour': forms.Select(attrs={'class': 'form-control mb-3'}),
            'end_hour': forms.Select(attrs={'class': 'form-control mb-3'}),
        }


class DutyShiftForm(forms.ModelForm):
    class Meta:
        model = DutyShift
        fields = ['name', 'operating_shift', 'description', 'begin_day', 'end_day', 'location']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control mb-3'}),
            'operating_shift': forms.Select(attrs={'class': 'form-control mb-3'}),
            'description': forms.Select(attrs={'class': 'form-control mb-3'}),
            'begin_day': forms.Select(attrs={'class': 'form-control mb-3'}),
            'end_day': forms.Select(attrs={'class': 'form-control mb-3'}),
            'location': forms.Select(attrs={'class': 'form-control mb-3'}),
        }
 