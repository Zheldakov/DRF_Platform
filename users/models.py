from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, }

class UserRoles(models.TextChoices):
    """Роли пользователей"""
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')
