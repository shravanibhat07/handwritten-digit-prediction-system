"""
URL configuration for GUI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from basics.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("abc/",abc,name="abc"),
    path("led/",led,name="led"),
    path("counter/",counter,name="counter"),
   path("calculator/",calculator,name="calculator"),
   path("calci/",calci,name="calci"),
   path("Employee/",Employee,name="Employee"),
   path("Employee1/",Employee1,name="Employee1"),
   path("student/",student,name="student"),
   path("Employee_View/",Employee_View,name="Employee_View"),
   path("Employee_update/<id>",Employee_update,name="Employee_update"),
   path("Employee_delete/<id>",Employee_delete,name="Employee_update"),
   path("index/",index,name="index"),
   path("predict1/",predict1,name="predict1"),
   path("recognition/",recognition,name="recognition"),
]
