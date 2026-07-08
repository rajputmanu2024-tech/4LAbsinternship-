

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'Raju', 'age': 20, 'city': 'Bangalore'},
        {'name': 'satyam', 'age': 52, 'city': 'Hyderabad'},
        {'name': 'mannan', 'age': 45, 'city': 'Delhi'},
        {'name': 'vijay', 'age': 14, 'city': 'Gurgaon'},
        {'name': 'shivam', 'age': 17, 'city': 'Mumbai'},
        {'name': 'kartik', 'age': 70, 'city': 'Chennai'},
        {'name': 'prakhar', 'age': 30, 'city': 'Kolkata'},
    ]

    context = {
        "page": "Home",
        "peoples": peoples,
    }
    
    return render(request, 'home/index.html', context)


def about_page(request):
    context = {"page": "About"}
    return render(request, 'home/about.html', context)

def contacts_page(request):
    context = {"page": "Contacts"}
    return render(request, 'home/contacts.html', context)