from django.db import models
from .managers import UserAccountManager 
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser,PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True,editable=False)
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    full_name = models.CharField(verbose_name=_('Full Name'),max_length=200)
    email = models.EmailField(verbose_name=_('Email Address'),unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['full_name']

    objects = UserAccountManager 

    class Meta:
        verbose_name = _('User Account')
        verbose_name_plural = _('User Account')

    def __str__(self):
        return self.full_name 
    
