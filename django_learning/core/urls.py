"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from . import views

from home.views import *
from vege.views import *
from student.views import *

app_name = 'student'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_page, name='about'),
    path('contacts/', contacts_page, name='contacts'),

    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),


    path('student/', student_list, name='student_list'),\
    path(' ', student_home, name='student_home'),
    

    path('recipes/', recipes, name='recipes'),
    path('delete_recipe/<int:recipe_id>/', delete_recipe, name='delete_recipe'),
    path('update_recipe/<int:recipe_id>/', update_recipe, name='update_recipe'),
    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)