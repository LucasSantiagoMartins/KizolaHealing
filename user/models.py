from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Email field must be set')

        normalized_email = self.normalize_email(email)
        user = self.model(email=normalized_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if not extra_fields.get('is_staff'):
            raise ValueError('is_staff field must be set')
        if not extra_fields.get('is_superuser'):
            raise ValueError('is_superuser field must be set')
        
        self.create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager

    USERNAME_FIELD = ('email')
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username