from rest_framework import serializers
from blog import models


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ("title", "main_photo", "created_ad")


class PostGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostGallery
        fields = ("image",)


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    blogs = PostGallerySerializer(many=True, read_only=True)

    class Meta:
        model = models.Post
        fields = ("title", "description", "author", "created_ad", "blogs")


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mail
        fields = ("email",)

    def create(self, validated_data):
        email = validated_data.get("email")
        try:
            return models.Mail.objects.create(email=email)
        except:
            raise "Error"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ("full_name", "email", "message")

    def create(self, validated_data):
        full_name = validated_data.get("full_name")
        email = validated_data.get("email")
        message = validated_data.get("message")

        return models.Contact.objects.create(full_name=full_name, email=email, message=message)
