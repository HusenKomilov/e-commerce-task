from django.db import models
from utils.models import BaseModel
from users.models import User


class Category(BaseModel):
    title = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to="category/")
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    width = models.IntegerField()
    height = models.IntegerField()
    length = models.IntegerField()
    weight = models.FloatField()

    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    is_new = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)

    category = models.ManyToManyField(Category, related_name="categories")

    def get_first_photo(self):
        if self.images:
            try:
                return self.images.first()
            except:
                return "-"
        else:
            return "-"

    def __str__(self):
        return self.title


class Gallery(BaseModel):
    image = models.ImageField(upload_to="products/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")


class Review(BaseModel):
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_review")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")

    def __str__(self):
        return self.user.username


class FavouriteProducts(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="like")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return self.product.title
