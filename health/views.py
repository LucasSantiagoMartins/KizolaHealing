from django.shortcuts import render
from .forms import InstitutionalInformationForm


def integrate_institution_view(request):
    if request.method == 'GET':
        context = {}
        context['form'] = InstitutionalInformationForm
        return render(request, 'integrate_institution.html', context)
