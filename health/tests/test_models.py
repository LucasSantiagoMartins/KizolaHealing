from health.models import (
    AdministrativeInformation,
    InstitutionalInformation,
    CertificationDocument,
    OperationInformation,
    ContactInformation,
    PolicyInformation,
    LicenseDocument,
    ServiceOffered,
    OperatingShift,
    Certification,
    OperatingHour,
    DutyShift,
    Address,
    License,
    Phone
)
from .mock_institution import MockInstitution 
from django.db import IntegrityError
from .file_handler import FileMock, TestWithFileMock
from django.test import TestCase
import os


class InstitutionTest(TestCase):
    def setUp(self):

        self.institution = MockInstitution.create()
        
        self.license = License.objects.create(
            license_title = 'LCF',
            license_number = '12345678910',
            license_status = 'ATV',
            issue_date = '2000-03-20',
            expiration_date = '2005-03-10',
            issuing_authority = 'issuing_authority_test',
            renewal_required = True,
            renewal_date = '2003-02-20',
            scope = 'scope_test',
            institution = self.institution
        )

        self.certification = Certification.objects.create(
            certification_title = 'CCI',
            certification_number = '12345678910',
            certification_status = 'ATV',
            issue_date = '2020-10-20',
            expiration_date = '2023-10-20',
            issuing_authority = 'issuing_authority_test',
            renewal_required = True,
            renewal_date = '2022-10-20',
            scope = 'scope_test',
            institution = self.institution       
        )

        self.policy_information = PolicyInformation.objects.create(
            title = 'PPD',
            description = 'description test',
            implementation_date = "2000-02-10",
            last_review_date = "2005-03-20",
            institution = self.institution
        )
    
    def test_institutional_information_relationship(self):
        self.assertEqual(self.institution.institutional_informations.institution_name, 'Hospital-test')
        
    def test_address_relationship(self):
        self.assertEqual(self.institution.address.street_address, 'Avenida 1º de Maio, 120')
    
    def test_administrative_information_relationship(self):
        self.assertEqual(self.institution.administrative_informations.responsible_person_email, 'johndoe@gmail.com')

    def test_operation_information_relationship(self):
        self.assertEqual(self.institution.operation_informations.id, 1)

    def test_policy_information_relationship(self):
        self.assertEqual(self.institution.policy_informations.all().count(), 1)
    
    def test_license_relationship(self):
        self.assertEqual(self.institution.licenses.all().count(), 1)

    def test_certification_relationship(self):
        self.assertEqual(self.institution.certifications.all().count(), 1)


class InstitutionalInformationTest(TestCase):
    def setUp(self):
        self.institutional_information = InstitutionalInformation.objects.create(
            institution_name = 'Hospital-test',
            # This nif is random
            nif = '5401137796',
            institution_type = 'HPG',
            founding_date = '2010-02-19'
        )
   
    def test_institution_name_check(self):
        self.assertEqual(self.institutional_information.institution_name, 'Hospital-test')
    
    def test_nif_check(self):
        self.assertEqual(self.institutional_information.nif, '5401137796')
    
    def test_institution_type_check(self):
        self.assertEqual(self.institutional_information.institution_type, 'HPG')
    
    def test_founding_date_check(self):
        self.assertEqual(self.institutional_information.founding_date, '2010-02-19')


class AddressTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            street_address = 'Avenida 1º de Maio, 120',
            neighborhood = 'Kilamba Kiaxi',
            province = 'Luanda'
        )
    
    def test_street_address_check(self):
        self.assertEqual(self.address.street_address, 'Avenida 1º de Maio, 120')

    def test_neighborhood_check(self):
        self.assertEqual(self.address.neighborhood, 'Kilamba Kiaxi')
    
    def test_province_chekc(self):
        self.assertEqual(self.address.province, 'Luanda')


class ContactInformationTest(TestCase):
    def setUp(self):

        mock_institution = MockInstitution.create()

        self.contact_information = ContactInformation.objects.create(
            email = 'kizolahealing@test.com',
            website = 'https://kizolahealing.com',
            related_institution = mock_institution
        )

    def test_email_check(self):
        self.assertEqual(
            self.contact_information.email,
            'kizolahealing@test.com'
        )

    def test_website_check(self):
        self.assertEqual(
            self.contact_information.website,
            'https://kizolahealing.com'
        )

    def test_institution_relationship(self):
        self.assertEqual(self.contact_information.related_institution.id, 1)
        
class PhoneTest(TestCase):
    def setUp(self):

        mock_institution = MockInstitution.create()

        self.contact_information = ContactInformation.objects.create(
            email = 'kizolahealing@test.com',
            website = 'https://kizolahealing.com',
            related_institution = mock_institution
        )

        self.phone = Phone.objects.create(
            phone_type = 'TFP',
            number = '834729573',
            contact_information = self.contact_information
        )

    def test_phone_contact_information_relationship(self):
        self.assertEqual(self.phone.contact_information.email, 'kizolahealing@test.com')

    def test_phone_check(self):
        self.assertEqual(self.phone.phone_type, 'TFP')
    
    def test_number_check(self):
        self.assertEqual(self.phone.number, '834729573')


class AdministrativeInformationTest(TestCase):
    def setUp(self):
        self.administrative_information = AdministrativeInformation.objects.create(
            responsible_person_name = 'John doe',
            responsible_person_nif = '033485838LA049',
            responsible_person_email = 'johndoe@gmail.com',
            responsible_person_phone = '936583451'
        )
    
    def test_responsible_person_name_check(self):
        self.assertEqual(
            self.administrative_information.responsible_person_name,
            'John doe'
        )

    def test_responsible_person_nif_check(self):
        self.assertEqual(
            self.administrative_information.responsible_person_nif,
            '033485838LA049'
        )
    
    def test_responsible_person_email_check(self):
        self.assertEqual(
            self.administrative_information.responsible_person_email,
            'johndoe@gmail.com'
        )
    
    def test_responsible_person_phone_check(self):
        self.assertEqual(
            self.administrative_information.responsible_person_phone,
            '936583451'
        )

class PolicyInformationTest(TestCase):
    def setUp(self):
        self.institution = MockInstitution.create()

        self.policy_information = PolicyInformation.objects.create(
            title = 'PPD',
            description = 'description test',
            implementation_date = "2000-02-10",
            last_review_date = "2005-03-20",
            institution = self.institution
        )

    def test_title_check(self):
        self.assertEqual(self.policy_information.title, 'PPD')

    def test_description_check(self):
        self.assertEqual(self.policy_information.description, 'description test')
    
    def test_implmentation_date_check(self):
        self.assertEqual(self.policy_information.implementation_date, '2000-02-10')
    
    def test_last_review_date_check(self):
        self.assertEqual(self.policy_information.last_review_date, '2005-03-20')

    def test_institution_relationship(self):
        self.assertEqual(self.policy_information.institution.id, 1)
    
    def test_uploads_document_successfully(self):
    
        image_mock = FileMock.create()

        self.policy_information.document = image_mock
        self.policy_information.save()
        
        self.assertIsInstance(PolicyInformation.objects.get(id=1), PolicyInformation)

        image_path = FileMock.get_file_path(self.policy_information.document.name)
        
        self.assertTrue(os.path.exists(image_path))
        # delete test document file
        FileMock.delete(image_path)


class LicenseTest(TestCase):
    def setUp(self):
        
        self.institution = MockInstitution.create()
    
        self.license = License.objects.create(
            license_title = 'LCF',
            license_number = '12345678910',
            license_status = 'ATV',
            issue_date = '2000-03-20',
            expiration_date = '2005-03-10',
            issuing_authority = 'issuing_authority_test',
            renewal_required = True,
            renewal_date = '2003-02-20',
            scope = 'scope_test',
            institution = self.institution
        )
        
        self.license_document_fields = {
            'related_license': self.license,
            'description': 'description_test'
        }

    def test_reverse_relationship_with_license_document(self):
        license_document = TestWithFileMock.create_object(LicenseDocument, self.license_document_fields, 'file')
        self.assertEqual(self.license.documents.all().count(), 1)
        TestWithFileMock.delete_uploaded_file_mock(license_document.file.name)

    def test_license_title_check(self):
        self.assertEqual(self.license.license_title, 'LCF')
    
    def test_license_number_check(self):
        self.assertEqual(self.license.license_number, '12345678910')
    
    def test_license_status_check(self):
        self.assertEqual(self.license.license_status, 'ATV')

    def test_issue_date_check(self):
        self.assertEqual(self.license.issue_date, '2000-03-20')
    
    def test_expiration_date_check(self):
        self.assertEqual(self.license.expiration_date, '2005-03-10')

    def test_issuing_authority_check(self):
        self.assertEqual(self.license.issuing_authority, 'issuing_authority_test')
    
    def test_renewal_required_check(self):
        self.assertTrue(self.license.renewal_required)

    def test_renewal_date_check(self):
        self.assertEqual(self.license.renewal_date, '2003-02-20')
    
    def test_scope_check(self):
        self.assertEqual(self.license.scope, 'scope_test')

    def test_license_document_uploads_document_successfully(self):
        license_document = TestWithFileMock.create_object(LicenseDocument, self.license_document_fields, 'file')
        image_path = FileMock.get_file_path(license_document.file.name)
        self.assertTrue(os.path.exists(image_path))
        TestWithFileMock.delete_uploaded_file_mock(license_document.file.name)

    def test_institution_realtionship(self):
        self.assertEqual(self.license.institution.id, 1)


class LicenseDocumentTest(TestCase):
    def setUp(self):
        self.institution = MockInstitution.create()

        self.related_license = License.objects.create(
            license_title = 'LCF',
            license_number = '12345678910',
            license_status = 'ATV',
            issue_date = '2000-03-20',
            expiration_date = '2005-03-10',
            issuing_authority = 'issuing_authority_test',
            renewal_required = True,
            renewal_date = '2003-02-20',
            scope = 'scope_test',
            institution = self.institution
        )

        self.license_document_fields = {
            'related_license': self.related_license,
            'description': 'description_test'
        }
    
    def test_license_document_license_relationship(self):
        license_document = TestWithFileMock.create_object(LicenseDocument, self.license_document_fields, 'file')
        self.assertEqual(license_document.related_license.license_title, 'LCF')
        TestWithFileMock.delete_uploaded_file_mock(license_document.file.name)

    def test_license_document_uploads_document_successfully(self):
        license_document = TestWithFileMock.create_object(LicenseDocument, self.license_document_fields, 'file')
        image_path = FileMock.get_file_path(license_document.file.name)
        self.assertTrue(os.path.exists(image_path))
        TestWithFileMock.delete_uploaded_file_mock(license_document.file.name)

    def test_description_check(self):
        license_document = TestWithFileMock.create_object(LicenseDocument, self.license_document_fields, 'file')
        self.assertEqual(license_document.description, 'description_test')
        TestWithFileMock.delete_uploaded_file_mock(license_document.file.name)
    
    def test_institution_realtionship(self):
        self.assertEqual(self.related_license.institution.id, 1)
    

class CertificationTest(TestCase):
    def setUp(self):

        self.institution = MockInstitution.create()
        self.fields = {
            'certification_title': 'CCI',
            'certification_number': '12345678910',
            'certification_status': 'ATV',
            'issue_date': '2020-10-20',
            'expiration_date': '2023-10-20',
            'issuing_authority': 'issuing_authority_test',
            'renewal_required': True,
            'renewal_date': '2022-10-20',
            'scope': 'scope_test',
            'institution': self.institution
        }
        self.certification = Certification.objects.create(**self.fields)

        self.certification_document_fields = {
            'related_certification': self.certification,
            'description': 'description_test'
        }

    def test_reverse_relationship_with_certification_document(self):
        certification_document = TestWithFileMock.create_object(
            CertificationDocument, 
            self.certification_document_fields,
            'file'
        )

        self.assertEqual(self.certification.documents.all().count(), 1)
        TestWithFileMock.delete_uploaded_file_mock(certification_document.file.name)

    def test_certification_title_check(self):
        self.assertEqual(self.certification.certification_title, 'CCI')

    def test_certification_number_check(self):
        self.assertEqual(self.certification.certification_number, '12345678910')
        
        with self.assertRaises(IntegrityError):
            # create certification with the same certification_number
            Certification.objects.create(**self.fields)

    def test_certification_status_check(self):
        self.assertEqual(self.certification.certification_status, 'ATV')
    
    def test_issue_date_check(self):
        self.assertEqual(self.certification.issue_date, '2020-10-20')

    def test_expiration_date_check(self):
        self.assertEqual(self.certification.expiration_date, '2023-10-20')

    def test_issuing_authority_check(self):
        self.assertEqual(self.certification.issuing_authority, 'issuing_authority_test')
    
    def test_renewal_required_check(self):
        self.assertTrue(self.certification.renewal_required)
        
    def test_renewal_date_check(self):
        self.assertEqual(self.certification.renewal_date, '2022-10-20')
    
    def test_renewal_date_check(self):
        self.assertEqual(self.certification.renewal_date, '2022-10-20')
    
    def test_scope_check(self):
        self.assertEqual(self.certification.scope, 'scope_test')
    
    def test_certification_document_uploads_document_successfully(self):
        certification_document = TestWithFileMock.create_object(
            CertificationDocument, 
            self.certification_document_fields,
            'file'
        )

        self.assertTrue(os.path.exists(FileMock.get_file_path(certification_document.file.name)))
        TestWithFileMock.delete_uploaded_file_mock(certification_document.file.name)
    
    def test_institution_relationship(self):
        self.assertEqual(self.certification.institution.id, 1)

class CertificationDocumentTest(TestCase):
    def setUp(self):
        self.institution = MockInstitution.create()

        self.certification = Certification.objects.create(
            certification_title = 'CCI',
            certification_number = '12345678910',
            certification_status = 'ATV',
            issue_date = '2020-10-20',
            expiration_date = '2023-10-20',
            issuing_authority = 'issuing_authority_test',
            renewal_required = True,
            renewal_date = '2022-10-20',
            scope = 'scope_test',
            institution = self.institution
        )

        self.certification_document_fields = {
            'related_certification': self.certification,
            'description': 'description_test'
        }

    def test_relationship_with_certification_document(self):
        certification_document = TestWithFileMock.create_object(
            CertificationDocument, 
            self.certification_document_fields,
            'file'
        )
        TestWithFileMock.delete_uploaded_file_mock(certification_document.file.name)
        self.assertEqual(certification_document.related_certification.certification_title, 'CCI')

    def test_certification_document_uploads_document_successfully(self):
        certification_document = TestWithFileMock.create_object(
            CertificationDocument, 
            self.certification_document_fields,
            'file'
        )

        self.assertTrue(os.path.exists(FileMock.get_file_path(certification_document.file.name)))
        TestWithFileMock.delete_uploaded_file_mock(certification_document.file.name)

    def test_description_test_check(self):
        certification_document = TestWithFileMock.create_object(
            CertificationDocument, 
            self.certification_document_fields,
            'file'
        )
        TestWithFileMock.delete_uploaded_file_mock(certification_document.file.name)
        self.assertEqual(certification_document.description, 'description_test')
    
    def test_institution_relationship(self):
        self.assertEqual(self.certification.institution.id, 1)


class OperationShiftTest(TestCase):
    def setUp(self):
        self.service_offered = ServiceOffered.objects.create(
            service_name = 'CTM',
            description = 'description_test'
        )

        self.operation_information = OperationInformation.objects.create()
        self.operation_information.services_offered.add(self.service_offered)
        self.operation_information.save()

        self.operating_shift = OperatingShift.objects.create(
            shift_type = 'TND',
            begin_hour = '16h',
            end_hour = '22h',
            operation_information = self.operation_information
        )

    def test_duration_property_returns_correct_string(self):
        self.assertEqual(self.operating_shift.duration, 'Das 16:00 às 22:00.')

    def test_relationship_with_operation_information(self):
        self.assertEqual(self.operating_shift.operation_information.id, 1)

    def test_shift_type_check(self):
        self.assertEqual(self.operating_shift.shift_type, 'TND')
    
    def test_begin_hour_check(self):
        self.assertEqual(self.operating_shift.begin_hour, '16h')
    
    def test_end_hour_check(self):
        self.assertEqual(self.operating_shift.end_hour, '22h')


class DutyShiftTest(TestCase):
    def setUp(self):
        self.service_offered = ServiceOffered.objects.create(
            service_name = 'CTM',
            description = 'description_test'
        )

        self.operation_information = OperationInformation.objects.create()
        self.operation_information.services_offered.add(self.service_offered)
        self.operation_information.save()

        self.operating_shift = OperatingShift.objects.create(
            shift_type = 'TND',
            begin_hour = '16h',
            end_hour = '22h',
            operation_information = self.operation_information
        )

        self.duty_shift = DutyShift.objects.create(
            name = 'duty shift A',
            operating_shift = self.operating_shift,
            description = 'description_test',
            begin_day = 'SD',
            end_day = 'DG',
            operation_information = self.operation_information
        )

    def test_str_method_returns_correct_string(self):
        self.assertEqual(str(self.duty_shift), 'Sábado à Domingo: Das 16:00 às 22:00.')

    def test_name_check(self):
        self.assertEqual(self.duty_shift.name, 'duty shift A')
    
    def test_description_check(self):
        self.assertEqual(self.duty_shift.description, 'description_test')

    def test_begin_day_check(self):
        self.assertEqual(self.duty_shift.begin_day, 'SD')
    
    def test_end_day(self):
        self.assertEqual(self.duty_shift.end_day, 'DG')
    
    def test_operation_information_relationship(self):
        self.assertEqual(self.duty_shift.operation_information.id, 1)
    
    def test_operating_shift_relationship(self):
        self.assertEqual(self.duty_shift.operating_shift.id, 1)

class OperatingHourTest(TestCase):
    def setUp(self):
        self.service_offered = ServiceOffered.objects.create(
            service_name = 'CTM',
            description = 'description_test'
        )

        self.operation_information = OperationInformation.objects.create()
        self.operation_information.services_offered.add(self.service_offered)
        self.operation_information.save()
    
        self.operating_hour = OperatingHour.objects.create(
            operating_hour = 'HMP',
            begin_day = 'SF',
            end_day = 'DG',
            begin_hour = '10h',
            end_hour = '22h',
            operation_information = self.operation_information,
            
        )
    
    def test_operating_hour_check(self):
        self.assertEqual(self.operating_hour.operating_hour, 'HMP')
    
    def test_begin_day_check(self):
        self.assertEqual(self.operating_hour.begin_day, 'SF')
    
    def test_end_day_check(self):
        self.assertEqual(self.operating_hour.end_day, 'DG')
    
    def test_begin_hour_check(self):
        self.assertEqual(self.operating_hour.begin_hour, '10h')
    
    def test_end_hour_check(self):
        self.assertEqual(self.operating_hour.end_hour, '22h')
    
    def test_operation_information_relationship(self):
        self.assertIsInstance(self.operating_hour.operation_information, OperationInformation)


class OperationInformationTest(TestCase):
    def setUp(self):
        self.service_offered = ServiceOffered.objects.create(
            service_name = 'CTM',
            description = 'description_test'
        )

        self.operation_information = OperationInformation.objects.create()
        self.operation_information.services_offered.add(self.service_offered)
        self.operation_information.save()

        self.operating_hour = OperatingHour.objects.create(
            operating_hour = 'HMP',
            begin_day = 'SF',
            end_day = 'DG',
            begin_hour = '10h',
            end_hour = '22h',
            operation_information = self.operation_information,
            
        )

        self.operating_shift = OperatingShift.objects.create(
            shift_type = 'TND',
            begin_hour = '16h',
            end_hour = '22h',
            operation_information = self.operation_information
        )

        self.duty_shift = DutyShift.objects.create(
            name = 'duty shift A',
            operating_shift = self.operating_shift,
            description = 'description_test',
            begin_day = 'SD',
            end_day = 'DG',
            operation_information = self.operation_information
        )
    
    def test_services_offered_relationship(self):
        self.assertEqual(self.operation_information.services_offered.all().count(), 1)
    
    def test_reverse_realationship_with_operating_shift(self):
        self.assertEqual(self.operation_information.operating_shifts.all().count(), 1)

    def test_reverse_realationship_with_duty_shift(self):
        self.assertEqual(self.operation_information.duty_shifts.all().count(), 1)

    def test_reverse_realationship_with_operating_hour(self):
        self.assertEqual(self.operation_information.operating_hours.all().count(), 1)
