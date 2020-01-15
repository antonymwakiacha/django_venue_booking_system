# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
"""Declare models for YOUR_APP app."""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, reg_no, password, **extra_fields):
        """Create and save a User with the given reg_no and password."""
        if not reg_no:
            raise ValueError('The given reg_no must be set')
        #reg_no = self.normalize_reg_no(reg_no)
        user = self.model(reg_no=reg_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, reg_no, password=None, **extra_fields):
        """Create and save a regular User with the given reg_no and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(reg_no, password, **extra_fields)

    def create_superuser(self, reg_no, password, **extra_fields):
        """Create and save a SuperUser with the given reg_no and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(reg_no, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    reg_no = models.CharField(_('reg_no'), unique=True,max_length=254)

    USERNAME_FIELD = 'reg_no'
    REQUIRED_FIELDS = []

    objects = UserManager()