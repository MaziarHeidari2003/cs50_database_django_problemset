from django.contrib import admin
from .models import Category,User,Bid,Listing,Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Comment)