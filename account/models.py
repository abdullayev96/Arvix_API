from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken
from .manager import UserManager



class CustomUser(AbstractUser):
      username = models.CharField(max_length=300)
      email =  models.EmailField(unique=True, blank=True)
      full_name = models.CharField(max_length=255,  verbose_name="Ism Familyasi:")
      middle_name = models.CharField(max_length=255, verbose_name="Otasini ismi:")
      number = models.CharField(max_length=255,  verbose_name="Telefon raqami:")
      otp = models.CharField(max_length=6, blank=True, null=True)
      active = models.BooleanField(default=True)
      staff = models.BooleanField(default=False)
      admin = models.BooleanField(default=False)



      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = []

      objects = UserManager()

      def __str__(self):
          return self.email




      def save(self, *args, **kwargs):
          try:
             if kwargs['password']:
                  self.set_password(kwargs['password'])
          except Exception:
                       pass
          finally:
                super(CustomUser, self).save(*args, **kwargs)



      class Meta:
          verbose_name = "Foydalanuvchi_"

