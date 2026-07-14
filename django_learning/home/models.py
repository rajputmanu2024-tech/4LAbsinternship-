o

from django.db import models

# Create your models here.

class address(models.Model):
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"


class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default = None)
    email = models.EmailField()
    address = models.ForeignKey(address, on_delete=models.CASCADE)
   
    

    def __str__(self):
        return self.name