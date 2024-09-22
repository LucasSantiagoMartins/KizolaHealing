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
    InstitutionalInformation,
    CertificationDocument,
    Certification
)
from .mock_institution import MockInstitution
from .file_handler import FileMock
from django.test import TestCase
import os


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


class CertificationDocumentFormTest(TestCase):

    def setUp(self):

        institution = MockInstitution.create()

        self.related_certification = Certification.objects.create(
            certification_title = 'CCI',
            certification_number = '12345678910',
            certification_status = 'ATV',
            issue_date = '2020-10-20',
            expiration_date = '2023-10-20',
            issuing_authority = 'issuing_authority_test',
            renewal_required = True,
            renewal_date = '2022-10-20',
            scope = 'scope_test',
            institution = institution
        )
        
        self.file_mock = FileMock.create()

    def test_certification_document_form_valid_data(self):

        form = CertificationDocumentForm(data={
            'description': 'description_test',
            'related_certification': self.related_certification
        }, files={'file': self.file_mock})

        self.assertTrue(form.is_valid())

        certification_document = form.save(commit=False)
        certification_document.related_certification = self.related_certification
        certification_document.save()

        self.assertEqual(certification_document.description, 'description_test')
        
        file_path = FileMock.get_file_path(certification_document.file.name)
        FileMock.delete(file_path)
    
    def test_certification_document_form_invalid_data(self):

        form = CertificationDocumentForm(data={
            'description': '',
        }, files={'file': ''})

        self.assertFalse(form.is_valid())

        # description is optional field
        self.assertNotIn('description', form.errors)
        self.assertIn('file', form.errors)

    def test_certification_document_form_partial_update(self):

        certification_document = CertificationDocument.objects.create(
            file = self.file_mock,
            description = 'description_test',
            related_certification = self.related_certification
        )

        file_path = FileMock.get_file_path(certification_document.file.name)
        FileMock.delete(file_path)

        new_file_mock = FileMock.create()       
    
        form = CertificationDocumentForm(data={
            'description': 'description_test2',
        }, files={'file': new_file_mock}, instance=certification_document)
    
        self.assertTrue(form.is_valid())

        updated_certification_document = form.save()

        self.assertEqual(updated_certification_document.description, 'description_test2')
        self.assertEqual(certification_document.file.name, updated_certification_document.file.name)

        updated_file_path = FileMock.get_file_path(updated_certification_document.file.name)
        FileMock.delete(updated_file_path)