import uuid

from django.db import models


class ProductsList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    discount = models.BooleanField()
    oldPrice = models.CharField(null=True, max_length=20)
    description = models.CharField(null=True, max_length=1000)
    cloth = models.CharField(null=True, max_length=1000)
    addition = models.CharField(null=True, max_length=1000)
    course = models.CharField(null=True, max_length=200)
    image = models.ImageField(upload_to='img/', blank=True, null=True)


    def __str__(self):
        return self.name


class FilesProduct(models.Model):
    idProduct = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    file = models.FileField(upload_to='filesPDF/', null=True)


    def __str__(self):
        return self.idProduct



class CommentariesProduct(models.Model):
    idProduct = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=30)
    comment = models.CharField(max_length=800)
    image = models.ImageField(upload_to='img/', blank=True, null=True)

    def __str__(self):
        return self.idProduct



class CategoriesProduct(models.Model):
    idProduct = models.CharField(max_length=100)
    idCategories = models.CharField(max_length=100)

    def __str__(self):
        return self.idProduct


class CategoriesAll(models.Model):
    idCategories = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='img/', blank=True, null=True)

    def __str__(self):
        return self.name

