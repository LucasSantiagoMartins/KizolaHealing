from health.models import (
    AdministrativeInformation,
    InstitutionalInformation,
    CertificationDocument,
    ContactInformation,
    PolicyInformation,
    LicenseDocument,
    Certification,
    Address,
    License,
    Phone
)
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError
from django.test import TestCase
from django.conf import settings
from io import BytesIO
from PIL import Image
import os

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
        self.contact_information = ContactInformation.objects.create(
            email = 'kizolahealing@test.com',
            website = 'https://kizolahealing.com'
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
        
class PhoneTest(TestCase):
    def setUp(self):
        self.contact_information = ContactInformation.objects.create(
            email = 'kizolahealing@test.com',
            website = 'https://kizolahealing.com'
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
        self.policy_information = PolicyInformation.objects.create(
            title = 'PPD',
            description = 'description test',
            implementation_date = "2000-02-10",
            last_review_date = "2005-03-20",
        )

    def test_title_check(self):
        self.assertEqual(self.policy_information.title, 'PPD')

    def test_description_check(self):
        self.assertEqual(self.policy_information.description, 'description test')
    
    def test_implmentation_date_check(self):
        self.assertEqual(self.policy_information.implementation_date, '2000-02-10')
    
    def test_last_review_date_check(self):
        self.assertEqual(self.policy_information.last_review_date, '2005-03-20')
    
    def test_document_check(self):
        image = Image.new('RGB', (100, 100), color='blue')
        image_io = BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)

        image_mock = SimpleUploadedFile('test_image.jpeg', image_io.read(), content_type='image/jpeg')

        self.policy_information.document = image_mock
        self.policy_information.save()
        
        self.assertIsInstance(PolicyInformation.objects.get(id=1), PolicyInformation)

        document_path = settings.MEDIA_ROOT + f"/{self.policy_information.document.name}"

        self.assertTrue(os.path.exists(document_path))
        # delete test document file
        os.remove(document_path)


class LicenseTest(TestCase):
    def setUp(self):
        self.license = License.objects.create(
            license_title = 'LCF',
            license_number = '12345678910',
            license_status = 'ATV',
            issue_date = '2000-03-20',
            expiration_date = '2005-03-10',
            issuing_authority = 'issuing_authority_test',
            renewal_required = True,
            renewal_date = '2003-02-20',
            scope = 'scope_test'
        )
    
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


class LicenseDocumentTest(TestCase):
    def setUp(self):
        self.license_document = LicenseDocument(
            file = 'license_doc_image_test.jpeg',
            description = 'description_test'
        )
    
    def test_file_check(self):
        self.assertEqual(self.license_document.file, 'license_doc_image_test.jpeg')

    def test_description_check(self):
        self.assertEqual(self.license_document.description, 'description_test')

class CertificationTest(TestCase):
    def setUp(self):
        self.fields = {
            'certification_title': 'CCI',
            'certification_number': '12345678910',
            'certification_status': 'ATV',
            'issue_date': '2020-10-20',
            'expiration_date': '2023-10-20',
            'issuing_authority': 'issuing_authority_test',
            'renewal_required': True,
            'renewal_date': '2022-10-20',
            'scope': 'scope_test'
        }
        self.certification = Certification.objects.create(**self.fields)

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
    

class CertificationDocumentTest(TestCase):
    def setUp(self):
        self.certification_document = CertificationDocument(
            description='description_test'
        )
    
    def test_description_test_check(self):
        self.assertEqual(self.certification_document.description, 'description_test')