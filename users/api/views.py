from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from users.api import serializers

User = get_user_model()


class RegistrationAPIView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)

        if serializer.is_valid():
            serializer.save()
            user = serializer.data

            return Response({
                "data": user,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class TestLoginApiView(APIView):

    def post(self, request):

        data = request.data
        username_or_email = data.get('username_or_email')
        password = data.get('password')
        user = authenticate(email=username_or_email, password=password)

        if username_or_email is None or password is None:
            return None

        if "@" in username_or_email:
            pass
        else:
            user = authenticate(username=username_or_email, password=password)
        if not user:
            return Response({"message": "invalide username or password"}, status=204)
        try:

            user_token = get_tokens_for_user(user)

            response = {
                # "username_or_email": user.json(),
                "access_token": str(user_token.get("access")),
                "refresh_token": str(user_token.get("refresh"))
            }
            return Response(response)
        except Exception as e:
            raise e


class Profile(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            "msg": "ist worker"
        }
        return Response(data, status=status.HTTP_200_OK)


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = serializers.UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
