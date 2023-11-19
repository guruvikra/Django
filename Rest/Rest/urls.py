"""
URL configuration for Rest project.

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
from Rest import views

urlpatterns = [
    path("", views.base, name="base"),
    path('signup/',views.signupp,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('admin/', admin.site.urls,name="admin"),
    path('index/',views.Index,name="Index"),
    path('home/',views.Home,name="home"),
    path('base/',views.User,name="User"),
    path('register/',views.Register,name="register"),
    path('update/',views.update_review,name='update'),
    path('Savereview/',views.Savereviews,name='Savereviews'),
    path('updatreview/',views.updatereview,name='updatereview'),
    path("logout/", views.logoutpage, name="logout"),
    path('Fav/',views.Favourite,name='fav'),
    path('favlist/',views.Favlist,name='favlist'),
    path('delfav/',views.Del,name='favremove')
    # path('bookmark/',views.Favourites,name='bookmark')
]
