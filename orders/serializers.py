from rest_framework import serializers
from products.serializers import ProductDetailSerializer
from orders import models


class CartListSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()

    class Meta:
        model = models.Cart
        fields = ("product", "quantity")


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ("product", "quantity")
