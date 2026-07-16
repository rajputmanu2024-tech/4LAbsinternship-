from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = CloudinaryField("image")
    recipe_view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.recipe_name