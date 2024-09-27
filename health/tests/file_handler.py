from django.core.files.uploadedfile import SimpleUploadedFile
from string import ascii_letters
from django.conf import settings
from io import BytesIO
from PIL import Image
import random
import os


class FileMock:

    @staticmethod
    def create():
        allowed_extension = ['JPEG', 'PNG']
        colors = ['red', 'green', 'blue']

        choosed_extension = allowed_extension[random.randint(0, 1)]
        choosed_color = colors[random.randint(0,2)]
        random_filename = ''.join(random.choice(ascii_letters) for _ in range(6))

        file = Image.new('RGB', (100, 100), color=choosed_color)
        buffer = BytesIO()
        file.save(buffer, format=choosed_extension)
        buffer.seek(0)

        file_with_extension = random_filename + f'.{choosed_extension.lower()}'

        file_mock = SimpleUploadedFile(
            name=file_with_extension, 
            content=buffer.read(), 
            content_type=f'image/{choosed_extension}'
        )
        
        return file_mock
    
    @staticmethod
    def get_file_path(uploaded_file_name):
        file_path = settings.MEDIA_ROOT + f"/{uploaded_file_name}"

        return file_path
    
    @staticmethod
    def delete(file_path):
        os.remove(file_path)

# TODO rename this class name
class TestWithFileMock:
    """
        Example:
            -> 
                class Profile(models.Model):
                    name = ...
                    last_name = ...
                    profile_picture = ...

                # how to test this model using TestWithFileMock

                class YourTestCase(TestCase):
                    def setUp(self):
                        # define your model's fields variable here except the file field
                        self.profile_fields = {'name': 'john' 'last_name': 'doe'}
                    
                    def your_test_that_use_file_mock(self):
                        profile = TestWithFileMock.create_object(Profile, self.profile_fields, 'profile_picture')
                        # test here using the created object
                        TestWithFileMock.delete_uploaded_file_mock(profile.profile_picture.name)
            ->
    """

    @staticmethod
    def create_object(model, model_fields, file_field_name):
        image_mock = FileMock.create()
        model_fields[file_field_name] = image_mock
        obj = model.objects.create(**model_fields)
        
        return obj
    
    @staticmethod
    def delete_uploaded_file_mock(uploaded_file_mock_name):
        image_path = FileMock.get_file_path(uploaded_file_mock_name)
        # delete test document file
        FileMock.delete(image_path)