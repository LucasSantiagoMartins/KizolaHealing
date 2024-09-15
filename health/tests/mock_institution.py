from health.models import (
    AdministrativeInformation,
    InstitutionalInformation,
    OperationInformation,
    ServiceOffered,
    Institution,
    Address,
)

class MockInstitution:

    @staticmethod
    def create():
        institutional_information = InstitutionalInformation.objects.create(
            institution_name = 'Hospital-test',
            # This nif is random
            nif = '5401137796',
            institution_type = 'HPG',
            founding_date = '2010-02-19'
        )

        address = Address.objects.create(
            street_address = 'Avenida 1º de Maio, 120',
            neighborhood = 'Kilamba Kiaxi',
            province = 'Luanda'
        )

        administrative_information = AdministrativeInformation.objects.create(
            responsible_person_name = 'John doe',
            responsible_person_nif = '033485838LA049',
            responsible_person_email = 'johndoe@gmail.com',
            responsible_person_phone = '936583451'
        )

        service_offered = ServiceOffered.objects.create(
            service_name = 'CTM',
            description = 'description_test'
        )

        operation_information = OperationInformation.objects.create()
        operation_information.services_offered.add(service_offered)
        operation_information.save()

        institution = Institution.objects.create(
            institutional_informations = institutional_information,
            address = address,
            administrative_informations = administrative_information,
            operation_informations = operation_information
        )

        return institution
