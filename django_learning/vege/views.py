from urllib import request

from django.shortcuts import render, redirect,get_object_or_404
from .models import Recipe
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    
    
    return render(request, "home.html")

@login_required(login_url="login")
def recipes(request):

    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        recipe_description = request.POST.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        Recipe.objects.create(
            user=request.user,
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )

        return redirect("recipes")

    queryset = Recipe.objects.all()

    if request.GET.get("search"):
        queryset = queryset.filter(
            recipe_name__icontains=request.GET.get("search")
        )

    context = {
        "recipes": queryset
    }

    return render(request, "recipes.html", context)


@login_required(login_url="login")
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(
    Recipe,
    id=recipe_id,
    user=request.user
    )
    recipe.delete()
    return redirect('recipes')



@login_required(login_url="login")
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(
    Recipe,
    id=recipe_id,
    user=request.user
    )     

    if request.method == "POST":
        recipe.recipe_name = request.POST.get("recipe_name")
        recipe.recipe_description = request.POST.get("recipe_description")

        image = request.FILES.get("recipe_image")

        if image:
            recipe.recipe_image = image

        recipe.save()

        return redirect("recipes")

    context = {
        "recipe": recipe
    }

    return render(request, "update_recipe.html", context)


def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("recipes")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")

    return render(request, "login.html")


def logout_page(request):
    
    logout(request)
    return redirect("login")

def register_page(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Password mismatch
        if password != confirm_password:
            messages.error(request, "Password and Confirm Password do not match.")
            return render(request, "register.html")

        # Username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "register.html")

        # Email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, "register.html")

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    return render(request, "register.html")