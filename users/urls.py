from django.urls import path

from users.views import user_detail_view, user_redirect_view, user_update_view
from users.api import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register("user")

app_name = "users"

urlpatterns = [
    path("register/", views.RegistrationAPIView.as_view(), name="register"),
    path("login/", views.LoginApiView.as_view(), name="login"),
    path("me/", views.Profile.as_view()),

    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
