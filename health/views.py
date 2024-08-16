from django.shortcuts import render



def integrate_institution_view(request):
    if request.method == 'GET':
        return render(request, 'integrate_institution.html')
