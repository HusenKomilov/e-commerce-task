from django.urls import path
from products import views
from rest_framework import routers
from rest_framework_nested import routers

# router = routers.DefaultRouter()
# product_router = router.nes

urlpatterns = [
    path("category/", views.CategoryListAPIView.as_view()),
    path("category/<int:pk>/", views.CategoryRetriveAPIView.as_view()),

    path("product/", views.ProductListAPIView.as_view()),
    path("product/new/", views.ProductNewListAPIView.as_view()),
    path("product/<slug:slug>/", views.ProductDetailAPIView.as_view()),

]
