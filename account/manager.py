from django.contrib.auth.base_user import BaseUserManager



# class UserManager(BaseUserManager):
#     use_in_migrations = True
#
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('The given email must be set ')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#
#
#     def create_user(self,email, password=None, **extra_fields):
#         if not email:
#             raise ValueError(("The email must be set"))
#         email  = self.normalize_email(email)
#         user  = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have  is_staff=True'
#             )
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have  is_superuser=True')
#
#         return self._create_user(email, password, **extra_fields)



class UserManager(BaseUserManager):
    """Define a model manager for User model"""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# class UserManager(BaseUserManager):
#     def create_user(self, email, full_name, middle_name,number, password=None,
#                     is_admin=False, is_staff=False,
#                     is_active=True):
#         if not email:
#             raise ValueError("User must have an email")
#         if not password:
#             raise ValueError("User must have a password")
#
#         user = self.model(
#             email=self.normalize_email(email)
#         )
#
#         user.set_password(password)  # change password to hash
#         user.full_name = full_name
#         user.middle_name = middle_name
#         user.number = number
#         user.admin = is_admin
#         user.staff = is_staff
#         user.active = is_active
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, full_name, middle_name,number,password=None, **extra_fields):
#         if not email:
#             raise ValueError("User must have an email")
#         if not password:
#             raise ValueError("User must have a password")
#
#         user = self.model(
#             email=self.normalize_email(email)
#         )
#         user.full_name = full_name
#         user.set_password(password)
#         user.middle_name = middle_name
#         user.number = number
#         user.admin = True
#         user.staff = True
#         user.active = True
#         user.save(using=self._db)
#         return user