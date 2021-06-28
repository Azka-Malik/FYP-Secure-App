"""secureapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from UI import views as ab
from quiz import views as qa
from client import views as ca


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ab.Login,name="login"),
    path('logout/', ab.logoutUser, name="logout"),
    path('home/', ab.home,name="home"),
    path('create/', ab.create,name="create"),
    path('AdminR/', ab.AdminReq, name="AdminR"),
    path('Clientlogin/', ca.Clientlogin,name="Clientlogin"),
    path('Clientlogout/', ca.Clientlogout, name="Clientlogout"),
    path('CLhome/', ca.CLhome,name="CLhome"),
    path('ClientCreate/', ca.ClientCreate,name="ClientCreate"),
    path('question/', qa.question,name="question"),
    path('get_personality/', qa.get_personality, name="get_personality")

]
