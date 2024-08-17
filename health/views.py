from django.shortcuts import render
from .forms import (
    AdministrativeInformationForm,
    InstitutionalInformationForm,
    CertificationDocumentForm,
    OperationInformationForm,
    ContactInformationForm,
    PolicyInformationForm,
    LicenseDocumentForm,
    CertificationForm,
    ServiceTypeForm,
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
        context['operation_information_form'] = OperationInformationForm
        context['contact_information_form'] = ContactInformationForm
        context['policy_information_form'] = PolicyInformationForm
        context['license_document_form'] = LicenseDocumentForm
        context['certification_form'] = CertificationForm
        context['service_type_form'] = ServiceTypeForm
        context['license_form'] = LicenseForm
        context['address_form'] = AddressForm
        context['phone_form'] = PhoneForm

        return render(request, 'integrate_institution.html', context)
