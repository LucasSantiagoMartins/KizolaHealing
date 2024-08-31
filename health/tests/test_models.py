from django.test import TestCase
from health.models import (
    InstitutionalInformation
)


class InstitutionalInformationTestCase(TestCase):
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