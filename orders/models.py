from django.db import models
from utils.models import BaseModel
from users.models import Customer


class Cupon(BaseModel):
    title = models.CharField(max_length=128)
    min_price = models.DecimalField(max_digits=12, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Cart(BaseModel):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="prod")
    quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=0)

    class Meta:
        unique_together = ("product", "user")

    @property
    def get_product_price(self):
        product_price = self.product.price * self.quantity
        return product_price


class Order(BaseModel):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="order_user")
    shipping_fee = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    is_paid = models.BooleanField(default=0)

    address = models.ForeignKey("Address", on_delete=models.CASCADE, related_name="address")

    def get_cart_total_price(self):
        pass


class OrderItem(BaseModel):
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    user = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_product")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="item")


class ContactInformation(BaseModel):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Country(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class PaymentType(models.TextChoices):
    CREDIT_CARD = "Pay by Card Credit"
    PAYPAL = "Paypal"


class Payment(BaseModel):
    payment_type = models.CharField(max_length=128, choices=PaymentType.choices, default=PaymentType.CREDIT_CARD)
    card_number = models.BigIntegerField()
    expiration = models.CharField(max_length=8)
    cvc = models.IntegerField()

    def __str__(self):
        return self.card_number


class Address(BaseModel):
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128, blank=True, null=True)
    zip_code = models.CharField(max_length=128, blank=True, null=True)

    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country")
    contact = models.ForeignKey(ContactInformation, on_delete=models.CASCADE, related_name="information")

    use_data = models.BooleanField(default=False)

    def __str__(self):
        return self.street
