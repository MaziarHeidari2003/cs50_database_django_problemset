from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass



class Category(models.Model):
    category_name = models.CharField(max_length=300)

    def __str__(self):
        return self.category_name



class Bid(models.Model):
    bid = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='bid_user')


class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image_url = models.CharField(max_length=20000)
    is_active = models.BooleanField(default=True)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='listing_category')   
    owner = models.ForeignKey(User, on_delete=models.CASCADE , null=True, blank=True, related_name='listing_owner')
    watchlist = models.ManyToManyField(User, blank=True, related_name='user_watchlist')


    def __str__(self):
        return self.title
    


class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='author_comment' )
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE , null=True, blank=True, related_name='author_listing')
    message = models.CharField(max_length=10000)
