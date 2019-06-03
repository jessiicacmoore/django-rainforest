from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_in_cents = models.IntegerField()

    def __str__(self):
        return "{} - ${}".format(self.name, self.price_in_cents)