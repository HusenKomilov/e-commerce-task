from rest_framework import generics
from orders import models, serializers


class CartListAPIView(generics.ListAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartListSerializer


class CartCreateAPIView(generics.CreateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CartUpdateDestoyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer
