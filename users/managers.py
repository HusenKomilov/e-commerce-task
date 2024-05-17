from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email


class UserManager(BaseUserManager):
    def email_validator(self, email):
        if email:
            validate_email(email)
        else:
            raise ValueError("Email must be validated here")

    def create_user(self, name, username, email, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)

        if not name:
            raise ValueError("Enter your name")

        if not username:
            raise ValueError("Enter your username")

        if not email:
            raise ValueError("Enter your email")

        user = self.model(name=name, username=username, email=email)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, name, username, email, password, **extra_fields):
        user = self.create_user(name=name, username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.role = "admin"
        user.save(using=self.db)
        return user
