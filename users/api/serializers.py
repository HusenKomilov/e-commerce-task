from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User, Customer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("name", "username", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data.get("name"),
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            password=validated_data.get("password")
        )
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    username_or_email = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)
    access_token = serializers.CharField(max_length=256, read_only=True)
    refresh_token = serializers.CharField(max_length=256, read_only=True)

    class Meta:
        model = User
        fields = ("username_or_email", "password", "access_token", "refresh_token")

    def validate(self, data):
        username_or_email = data.get('username_or_email')
        password = data.get('password')
        print(data.get('password'))
        if username_or_email is None or password is None:
            return None

        if "@" in username_or_email:
            user = authenticate(email=username_or_email, password=password)

        else:
            user = authenticate(username=username_or_email, password=password)
        if not user:
            raise exceptions.AuthenticationFailed("invalide username or password")
        try:
            user_token = get_tokens_for_user(user)
            return {
                "access_token": str(user_token.get("access")),
                "refresh_token": str(user_token.get("refresh"))
            }
        except Exception as e:
            raise e


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "email", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("user", "image")


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ("user", "first_name", "last_name", "image")
