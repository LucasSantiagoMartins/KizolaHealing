from django.urls import path
from . import views

urlpatterns = [
    path('integrate-institution/', views.integrate_institution_view, name='intergrate_institution_url')
]
