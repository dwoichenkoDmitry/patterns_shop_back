from django.db import models

# Create your models here.
class BagProducts(models.Model):
    loginUser = models.CharField(max_length=255)
    idProduct = models.CharField(max_length=255)
    size = models.CharField(max_length=255)

    def __str__(self):
        return self.idProduct


class SaledProducts(models.Model):
    loginUser = models.CharField(max_length=255)
    idProduct = models.CharField(max_length=255)
    size = models.CharField(max_length=255)

    def __str__(self):
        return self.idProduct