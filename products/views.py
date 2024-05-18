from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from products import models, serializers, paginations, filters


class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()[:3]
    serializer_class = serializers.CategorySerializer


class CategoryRetriveAPIView(generics.RetrieveAPIView):
    queryset = models.Category.objects.prefetch_related("categories").all()
    serializer_class = serializers.CategoryRetriveSerializer


class ProductNewListAPIView(generics.ListAPIView):
    queryset = models.Product.objects.filter(is_new=True).order_by("?")[:7]
    serializer_class = serializers.ProductNewSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = models.Product.objects.all().order_by("-created_ad")
    serializer_class = serializers.ProductNewSerializer
    pagination_class = paginations.ProductListPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = filters.ProductFilter
    search_fields = ("category__title", "title")


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
    lookup_field = "slug"

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewsSerializer