from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import TimeStampedUUID
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
# Create your m

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(TimeStampedUUID):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+2348151573452"
    )
    address = models.TextField(verbose_name=_("Home Address"))
    gender = models.CharField(verbose_name=_('Gender'), choices=Gender.choices, default=Gender.OTHER,max_length=256)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"),
                                      upload_to='profile-photos', default='/profile-default.png')
    city = models.CharField(verbose_name=_("City"), max_length=256, default="Lagos", blank=False, null=False)
    country = models.CharField(verbose_name=_("Country"), max_length=256, default="Nigeria", blank=False, null=False)

    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profile'
