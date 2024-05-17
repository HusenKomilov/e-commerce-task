from rest_framework import generics
from blog import models, serializers, paginations


class PostListAPIView(generics.ListAPIView):
    queryset = models.Post.objects.all().order_by("?")
    serializer_class = serializers.PostListSerializer
    pagination_class = paginations.BlogPagination


class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostDetailSerializer


class PostRandomAPIView(generics.ListAPIView):
    queryset = models.Post.objects.all().order_by("?")[:3]
    serializer_class = serializers.PostListSerializer


class MailCreateAPIView(generics.CreateAPIView):
    queryset = models.Mail.objects.all()
    serializer_class = serializers.MailSerializer


class ContactCreateAPIView(generics.CreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
