from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, username, password, **extra_fields):
        if not phone_number:
            raise ValueError(_('Telefon raqam kiritilishi shart'))
        if not username:
            raise ValueError(_('Foydalanuvchi nomi kiritilishi shart'))
            
        user = self.model(
            phone_number=phone_number,
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_confirmed', False)
        return self._create_user(phone_number, username, password, **extra_fields)

    def create_superuser(self, phone_number, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_confirmed', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser uchun is_staff=True bo\'lishi kerak'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser uchun is_superuser=True bo\'lishi kerak'))

        return self._create_user(phone_number, username, password, **extra_fields)