from django_filters.rest_framework import FilterSet
from products import models


class ProductFilter(FilterSet):
    class Meta:
        model = models.Product
        fields = {
            "category": ["exact"],
            "price": ["gt", "lt"]
        }
