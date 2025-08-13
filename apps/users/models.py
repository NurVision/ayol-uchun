from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from django.utils.translation import gettext_lazy as _

from apps.users.choices import ReasonDeleteChoices
from apps.common.models import BaseModel

class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=30, verbose_name=_("Username"))
    email = models.EmailField(null=True, blank=True, verbose_name=_("Email"))

    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(
        unique=True,
        max_length=50,  # Increased to accommodate suffix
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
            )
        ],
        verbose_name=_("Phone number"),
    )
    bio = models.TextField(null=True, blank=True, verbose_name=_("Bio"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    is_confirmed = models.BooleanField(default=False, verbose_name=_("Is Confirmed"))
    is_deleted = models.BooleanField(default=False, verbose_name=_("Is Deleted"))
    reason_delete_choices = models.CharField(
        choices=ReasonDeleteChoices.choices,
        null=True,
        blank=True,
        verbose_name=_("Reason Delete Choice"),
    )
    reason_delete_str = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Reason Delete String")
    )
    interests = models.ManyToManyField("Interest", blank=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = [
        "username"
    ]

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = ("Users")

class Interest(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Interest")
        verbose_name_plural = _("Interests")