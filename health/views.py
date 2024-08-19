from django.shortcuts import render
from .forms import (
    AdministrativeInformationForm,
    InstitutionalInformationForm,
    CertificationDocumentForm,
    ContactInformationForm,
    PolicyInformationForm,
    LicenseDocumentForm,
    OperatingShiftForm,
    CertificationForm,
    OperatingHourForm,
    ServiceOfferedForm,
    DutyShiftForm,
    LicenseForm,
    AddressForm,
    PhoneForm,
)




def integrate_institution_view(request):
    if request.method == 'GET':
        context = {}
        context['administrative_information_form'] = AdministrativeInformationForm
        context['institutional_information_form'] = InstitutionalInformationForm
        context['certification_document_form'] = CertificationDocumentForm
        context['contact_information_form'] = ContactInformationForm
        context['policy_information_form'] = PolicyInformationForm
        context['license_document_form'] = LicenseDocumentForm
        context['operating_shift_form'] = OperatingShiftForm
        context['operating_hour_form'] = OperatingHourForm
        context['certification_form'] = CertificationForm
        context['service_offered_form'] = ServiceOfferedForm
        context['duty_shift_form'] = DutyShiftForm
        context['license_form'] = LicenseForm
        context['address_form'] = AddressForm
        context['phone_form'] = PhoneForm

        return render(request, 'integrate_institution.html', context)
