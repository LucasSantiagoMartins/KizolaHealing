from django import forms
from .models import (
    AdministrativeInformation,
    InstitutionalInformation, 
    CertificationDocument,
    ContactInformation,
    PolicyInformation,
    LicenseDocument,
    OperatingShift,
    Certification,
    OperatingHour,
    ServiceOffered,
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
            'institution_name': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_InstitutionalInformationForm_institution_name'}),
            'nif': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_InstitutionalInformationForm_nif'}),
            'institution_type': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_InstitutionalInformationForm_institution_type'}),
            'founding_date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date', 'id': 'id_InstitutionalInformationForm_founding_date'})
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        widgets = {
            'street_address': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_AddressForm_street_address'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_AddressForm_neighborhood'}),
            'province': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_AddressForm_province'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_AddressForm_postal_code'})
        }
       

class AdministrativeInformationForm(forms.ModelForm):
    class Meta:
        model = AdministrativeInformation
        fields = '__all__'
        widgets = {
            'responsible_person_name': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_AdministrativeInformationForm_responsible_person_name'}),
            'responsible_person_nif': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_AdministrativeInformationForm_responsible_person_nif'}),
            'responsible_person_email': forms.EmailInput(attrs={'class': 'form-control mb-3', 'id': 'id_AdministrativeInformationForm_responsible_person_email'}),
            'responsible_person_phone': forms.NumberInput(attrs={'class': 'form-control mb-3', 'id': 'id_AdministrativeInformationForm_responsible_person_phone'})
        }


class CertificationDocumentForm(forms.ModelForm):
    class Meta:
        model = CertificationDocument
        fields = ['file', 'description']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control mb-3', 'id': 'id_CertificationDocumentForm_file'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_CertificationDocumentForm_description'})
        }


class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3', 'id': 'id_ContactInformationForm_email'}),
            'website': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_ContactInformationForm_website'}),
        }


class PolicyInformationForm(forms.ModelForm):
    class Meta:
        model = PolicyInformation
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_PolicyInformationForm_title'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_PolicyInformationForm_description'}),
            'implementation_date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date', 'id': 'id_PolicyInformationForm_implementation_date'}),
            'last_review_date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date', 'id': 'id_PolicyInformationForm_last_review_date'}),
            'document': forms.FileInput(attrs={'class': 'form-control mb-3', 'id': 'id_PolicyInformationForm_document'})
        }


class LicenseDocumentForm(forms.ModelForm):
    class Meta:
        model = LicenseDocument
        fields = ['file', 'description']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control mb-3', 'id': 'id_LicenseDocumentForm_file'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_LicenseDocumentForm_description'})
        }


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'
        widgets = {
            'certification_title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Certification title...', 'id': 'id_CertificationForm_certification_title'}),
            'certification_number': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Certification number...', 'id': 'id_CertificationForm_certification_number'}),
            'certification_status': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_CertificationForm_certification_status'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date', 'id': 'id_CertificationForm_expiration_date'}),
            'issuing_authority': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Issuing authority...', 'id': 'id_CertificationForm_issuing_authority'}),
            'renewal_required': forms.CheckboxInput(attrs={'class': 'mb-3', 'id': 'id_CertificationForm_renewal_required'}),
            'renewal_date': forms.DateInput(attrs={'class': 'form-control mb-3','type': 'date', 'id': 'id_CertificationForm_renewal_date'}),
            'scope': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Scope...', 'id': 'id_CertificationForm_scope'})
        }
        

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = '__all__'
        widgets = {
            'license_title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Lincense title...', 'id': 'id_LicenseForm_license_title'}),
            'license_number': forms.NumberInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Lincense number...', 'id': 'id_LicenseForm_license_number'}),
            'license_status': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_LicenseForm_license_status'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date', 'id': 'id_LicenseForm_issue_date'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date', 'id': 'id_LicenseForm_expiration_date'}),
            'issuing_authority': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Issuing authority...', 'id': 'id_LicenseForm_issuing_authority'}),
            'renewal_required': forms.CheckboxInput(attrs={'class': 'mb-3', 'id': 'id_LicenseForm_renewal_required'}),
            'renewal_date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date', 'id': 'id_LicenseForm_renewal_date'}),
            'scope': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Scope...', 'id': 'id_LicenseForm_scope'})
        }


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['phone_type', 'number']
        widgets = {
            'phone_type': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_PhoneForm_phone_type'}),
            'number': forms.NumberInput(attrs={'class': 'form-control mb-3', 'id': 'id_PhoneForm_number'})
        }


class ServiceOfferedForm(forms.ModelForm):
    class Meta:
        model = ServiceOffered
        fields = '__all__'
        widgets = {
            'service_name': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_ServiceOfferedForm_service_name'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_ServiceOfferedForm_description'})
        }


class OperatingHourForm(forms.ModelForm):
    class Meta:
        model = OperatingHour
        fields = ['operating_hour', 'begin_day', 'end_day', 'begin_hour', 'end_hour']
        widgets = {
            'operating_hour': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_OperatingHourForm_operating_hour'}),
            'begin_day': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_OperatingHourForm_begin_day'}),
            'end_day': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_OperatingHourForm_end_day'}),
            'begin_hour': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_OperatingHourForm_begin_hour'}),
            'end_hour': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_OperatingHourForm_end_hour'}),
        }


class DutyShiftForm(forms.ModelForm):
    class Meta:
        model = DutyShift
        fields = ['name', 'operating_shift', 'description', 'begin_day', 'end_day', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Name...', 'id': 'id_DutyShiftForm_name'}),
            'operating_shift': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_DutyShiftForm_operating_shift'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Description...', 'id': 'id_DutyShiftForm_description'}),
            'begin_day': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_DutyShiftForm_begin_day'}),
            'end_day': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_DutyShiftForm_end_day'}),
            'location': forms.TextInput(attrs={'class': 'form-control mb-3', 'id': 'id_DutyShiftForm_location'}),
        }
 

class OperatingShiftForm(forms.ModelForm):
    class Meta:
        model = OperatingShift
        fields = ['shift_type', 'begin_hour', 'end_hour']
        widgets = {
            'shift_type': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_OperatingShiftForm_shift_type'}),
            'begin_hour': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_OperatingShiftForm_begin_hour'}),
            'end_hour': forms.Select(attrs={'class': 'form-control mb-3', 'id': 'id_OperatingShiftForm_end_hour'}),
        }

    