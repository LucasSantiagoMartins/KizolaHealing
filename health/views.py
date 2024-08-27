from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
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
    
    elif request.method == 'POST':
        forms = {
            'administrative_information_form': AdministrativeInformationForm(request.POST),
            'institutional_information_form': InstitutionalInformationForm(request.POST),
            'certification_document_form': CertificationDocumentForm(request.POST),
            'contact_information_form': ContactInformationForm(request.POST),
            'policy_information_form': PolicyInformationForm(request.POST),
            'license_document_form': LicenseDocumentForm(request.POST),
            'operating_shift_form': OperatingShiftForm(request.POST),
            'operating_hour_form': OperatingHourForm(request.POST),
            'certification_form': CertificationForm(request.POST),
            'service_offered_form': ServiceOfferedForm(request.POST),
            'duty_shift_form': DutyShiftForm(request.POST),
            'license_form': LicenseForm(request.POST),
            'address_form': AddressForm(request.POST),
            'phone_form': PhoneForm(request.POST)
        }

        for form in forms:
            if form.is_valid():
                form.save()

        messages.add_message(request, constants.SUCCES, 'Instituição integrada com sucesso')

        # The institution view isn't created
        return redirect(reverse('institution_view'))