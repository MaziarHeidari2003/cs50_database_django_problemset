from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,Category,Listing


def index(request):
    active_listings = Listing.objects.filter(is_active=True)
    all_categories = Category.objects.all()
    return render(request, "auctions/index.html",{
        "listings": active_listings,
        "categories": all_categories
    })


def listing(request, id):
    listing_data = Listing.objects.get(pk=id)
    return render(request, "auctions/listing.html", {
        "listing":listing_data
    })

def display_category(request):
    if request.method == "POST":
        category_from_form = request.POST['category']
        category = Category.objects.get(category_name=category_from_form)
        active_listings = Listing.objects.filter(is_active=True, category=category)
    all_categories = Category.objects.all()
    return render(request, "auctions/index.html",{
        "listings": active_listings,
        "categories": all_categories
    })


def create_listing(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        return render(request,"auctions/create.html", {
            "categories": all_categories
        }) 
    else:
        title = request.POST["title"]
        description = request.POST['description']
        imageurl = request.POST['imageurl']
        price = request.POST['price']
        category = request.POST['category']
        current_user = request.user

        category_data = Category.objects.get(category_name=category)

        new_listing = Listing(
            title=title,
            description=description,
            price=float(price),
            category=category_data,
            owner=current_user
        )
        new_listing.save()

        return HttpResponseRedirect(reverse('index'))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



