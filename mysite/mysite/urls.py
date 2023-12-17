"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path , include
from polls.views import table , data , form , first_page

urlpatterns = [
    path('polls/', include("polls.urls")),
    path('admin/', admin.site.urls),
    # path('your-name/', get_name , name='your_name'),
    path('time/', table , name='time'),
    path('data/', data , name='data'),
    path('form/', form , name='form'),
    path('' , first_page , name = 't'),


]
