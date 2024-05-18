from django.urls import path
from orders import views

urlpatterns = [
    path("card/", views.CartListAPIView.as_view()),
    path("card/create/", views.CartCreateAPIView.as_view()),
    path("card/<int:pk>/", views.CartUpdateDestoyAPIView.as_view())
]
