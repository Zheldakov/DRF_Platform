from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, }

class UserRoles(models.TextChoices):
    """Роли пользователей"""
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')

class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True,verbose_name='email')
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    first_name = models.CharField(max_length=150, verbose_name='First Name',default="Anonymous")
    last_name = models.CharField(max_length=150, verbose_name='Last Name', default="Anonymous")
    phone = models.CharField(max_length=35, verbose_name='Phone number', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='active', help_text='Активный пользователь')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']