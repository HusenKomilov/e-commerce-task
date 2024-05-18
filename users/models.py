from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db import models
from utils.models import BaseModel
from users import managers
from rest_framework_simplejwt.tokens import RefreshToken

USER = "user"
ADMIN = 'admin'
ROLES = [
    (ADMIN, "admin"),
    (USER, 'user')
]


class User(AbstractUser):
    name = models.CharField(max_length=128)
    username = models.CharField(max_length=128, unique=True)
    role = models.CharField(max_length=128, choices=ROLES, default=USER)
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name", "username", ]

    objects = managers.UserManager()

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access_token": str(refresh.access_token)
        }


class Customer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    first_name = models.CharField(max_length=128, default=None, null=True, blank=True)
    last_name = models.CharField(max_length=128, default=None, null=True, blank=True)

    image = models.ImageField(upload_to="profile", blank=True, null=True)

    def __str__(self):
        return self.user.username

