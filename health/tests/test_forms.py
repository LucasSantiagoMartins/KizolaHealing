from django.test import TestCase
from health.forms import (
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
from health.models import (
    AdministrativeInformation,
    InstitutionalInformation
)

class AdministrativeInformationFormTest(TestCase):

    def test_administrative_information_form_valid_data(self):
        form = AdministrativeInformationForm(data={
            'responsible_person_name': 'John doe',
            'responsible_person_nif': '033485838LA049',
            'responsible_person_email': 'johndoe@gmail.com',
            'responsible_person_phone': '936583451'
            
        })

        self.assertTrue(form.is_valid())

        administrative_information = form.save()
        self.assertEqual(administrative_information.responsible_person_name, 'John doe')
        self.assertEqual(administrative_information.responsible_person_nif, '033485838LA049')
        self.assertEqual(administrative_information.responsible_person_email, 'johndoe@gmail.com')
        self.assertEqual(administrative_information.responsible_person_phone, '936583451')
    
    def test_administrative_information_form_invalid_data(self):

        form = AdministrativeInformationForm(data={
            'responsible_person_name': '',
            'responsible_person_nif': '',
            'responsible_person_email': 'johndoe#gmailcom',
            'responsible_person_phone': 'aaaa'
            
        })

        self.assertFalse(form.is_valid())

        self.assertIn('responsible_person_name', form.errors)
        self.assertIn('responsible_person_nif', form.errors)
        self.assertIn('responsible_person_email', form.errors)
        self.assertIn('responsible_person_phone', form.errors)

    def test_administrative_information_form_partial_update(self):

        adm_information = AdministrativeInformation.objects.create(
            responsible_person_name = 'John doe',
            responsible_person_nif = '033485838LA049',
            responsible_person_email = 'johndoe@gmail.com',
            responsible_person_phone = '936583451'
        )  

        form = AdministrativeInformationForm(data={
            'responsible_person_name': 'John Smith',
            'responsible_person_nif': '033485838LA049',
            'responsible_person_email': 'johnsmith@gmail.com',
            'responsible_person_phone': '936583451'
        }, instance=adm_information)
    
        self.assertTrue(form.is_valid())

        updated_admn_information = form.save()

        self.assertEqual(updated_admn_information.responsible_person_name, 'John Smith')
        self.assertEqual(updated_admn_information.responsible_person_email, 'johnsmith@gmail.com')


class InstitutionalInformationFormTest(TestCase):

    def test_institutional_information_form_valid_data(self):
        form = InstitutionalInformationForm(data={
            'institution_name': 'Hospital-test',
            # This nif is random
            'nif': '5401137796',
            'institution_type': 'HPG',
            'founding_date': '2010-02-19'
            
        })

        self.assertTrue(form.is_valid())

        institutional_information = form.save()

        self.assertEqual(institutional_information.institution_name, 'Hospital-test')
        self.assertEqual(institutional_information.nif, '5401137796')
        self.assertEqual(institutional_information.institution_type, 'HPG')
        self.assertEqual(institutional_information.founding_date.strftime('%Y-%m-%d'), '2010-02-19')
    
    def test_institutional_information_form_invalid_data(self):

        form = InstitutionalInformationForm(data={
            'institution_name': '',
            # This nif is random
            'nif': '',
            'institution_type': 'ddd',
            'founding_date': '2010-03/20'
            
        })

        self.assertFalse(form.is_valid())

        self.assertIn('institution_name', form.errors)
        self.assertIn('nif', form.errors)
        self.assertIn('institution_type', form.errors)
        self.assertIn('founding_date', form.errors)

    def test_institutional_information_form_partial_update(self):

        institutional_information = InstitutionalInformation.objects.create(
            institution_name = 'Hospital-test',
            # This nif is random
            nif = '5401137796',
            institution_type = 'HPG',
            founding_date = '2010-02-19'
        )

        form = InstitutionalInformationForm(data={
            'institution_name': 'Hospital-test2',
            # This nif is random
            'nif': '5401137796',
            'institution_type': 'HPG',
            'founding_date': '2010-02-19'
            
        }, instance=institutional_information)
    
        self.assertTrue(form.is_valid())

        updated_institutional_information = form.save()

        self.assertEqual(updated_institutional_information.institution_name, 'Hospital-test2')