from django.db import models
import uuid
# Create your models here.

class Courses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/', blank=True, null=True)

    def __str__(self):
        return self.name