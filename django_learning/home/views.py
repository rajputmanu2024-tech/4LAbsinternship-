from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
   

    peoples=[{'name':'Raju','age':20, 'city':'Bangalore'},
             {'name':'satyam','age':52, 'city':'hyderabad'},
             {'name':'mannan','age':45, 'city':'delhi'},
             {'name':'vijay','age':14, 'city':'gurgaon'},
             {'name':'shivam','age':17, 'city':'mumbai'},
             {'name':'kartik','age':70, 'city':'chennai'},
             {'name':'prakhar','age':30, 'city':'kolkata'},]


    return render(request, 'index.html', {'peoples':peoples})


def about_page(request):
    return HttpResponse("This is about page")