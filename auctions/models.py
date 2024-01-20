from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name

class Listing(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image_url = models.CharField(max_length=1000)
    price = models.FloatField()
    is_active = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True, related_name="categpry")