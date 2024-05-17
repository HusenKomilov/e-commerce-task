from django.urls import path
from blog import views

urlpatterns = [
    path("", views.PostListAPIView.as_view()),
    path("random/", views.PostRandomAPIView.as_view()),
    path("<int:pk>/", views.PostRetrieveAPIView.as_view()),

    path("mail/", views.MailCreateAPIView.as_view()),
    path("contact/", views.ContactCreateAPIView.as_view()),
]
