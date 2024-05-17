from django.db import models
from utils.models import BaseModel
from users.models import User


class Post(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    main_photo = models.ImageField(upload_to="post/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def get_first_photo(self):
        if self.blog:
            try:
                return self.blog.first()
            except:
                return "-"
        else:
            return "-"

    def __str__(self):
        return self.title


class PostGallery(BaseModel):
    image = models.ImageField(upload_to="post/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="blogs")


class Contact(BaseModel):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name


class Mail(BaseModel):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
