from django.db import models

# Create your models here.
class Question(models.Model):
    first_name = models.CharField("First name", max_length=255)
    wayCalling = models.CharField("callType", max_length=20)
    callRealize = models.CharField("call realize", max_length=255)
    questionText = models.CharField("question text", max_length=255)

    def __str__(self):
        return self.callRealize