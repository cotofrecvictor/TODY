from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sarcini(models.Model):
    utilizator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titlu = models.CharField(max_length=50)
    completat = models.BooleanField(default=False)
    creat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titlu

