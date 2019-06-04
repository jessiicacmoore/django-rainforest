from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(500)])
    price_in_cents = models.IntegerField()

    def __str__(self):
        return "{} - ${}".format(self.name, self.price_in_cents)

    def price_in_dollars(self):
        dollars = self.price_in_cents / 100
        return "${:.2f}".format(dollars)


class Review(models.Model):
    message = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    