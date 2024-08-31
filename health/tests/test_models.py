from django.test import TestCase
from health.models import (
    AdministrativeInformation,
    InstitutionalInformation,
    ContactInformation,
    Address,
    Phone
)


#   ===== Unit tests =====
class InstitutionalInformationTest(TestCase):
    def setUp(self):
        self.institutional_information = InstitutionalInformation(
            institution_name = 'Hospital-test',
            # This nif is random
            nif = '5401137796',
            institution_type = 'HPG',
            founding_date = '19/02/2010'
        )

    def test_institution_name_check(self):
        self.assertEqual(self.institutional_information.institution_name, 'Hospital-test')
    
    def test_nif_check(self):
        self.assertEqual(self.institutional_information.nif, '5401137796')
    
    def test_institution_type_check(self):
        self.assertEqual(self.institutional_information.institution_type, 'HPG')
    
    def test_founding_date_check(self):
        self.assertEqual(self.institutional_information.founding_date, '19/02/2010')


class AddressTest(TestCase):
    def setUp(self):
        self.address = Address(
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
        self.contact_information = ContactInformation(
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
        self.phone = Phone(
            phone_type = 'TFP',
            number= '834729573'
        )
    
    def test_phone_check(self):
        self.assertEqual(self.phone.phone_type, 'TFP')
    
    def test_number_check(self):
        self.assertEqual(self.phone.number, '834729573')


class AdministrativeInformationTest(TestCase):
    def setUp(self):
        self.administrative_information = AdministrativeInformation(
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

    