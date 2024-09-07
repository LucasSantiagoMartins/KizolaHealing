from django.core.files.uploadedfile import SimpleUploadedFile
from string import ascii_letters
from django.conf import settings
import random
from io import BytesIO
from PIL import Image
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
        