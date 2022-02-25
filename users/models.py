from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from quiz import settings
import jwt

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, verbose_name="Логин")
    email = models.EmailField(
        max_length=255,
        validators=[validators.validate_email],
        blank=False,
        verbose_name="email",
    )

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ("email",)
    USERNAME_FIELD = "username"
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        some_data = {"id": self.pk, "exp": 1916239022}
        token = jwt.encode(some_data, settings.SECRET_KEY, algorithm="HS256")
        return token.decode("utf-8")

    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("Указаное имя пользователя должно быть установлено")
        if not email:
            raise ValueError("Данный адрес электронной почты должен быть установлен")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Администратор должен иметь is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Администратор должен иметь is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)
