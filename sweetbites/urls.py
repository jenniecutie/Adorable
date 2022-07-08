"""webdevSB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from sweetbites import views
from django.urls import re_path as url

urlpatterns = [
    path('', views.MainPage, name='mainpage'),
    path('recipe/', views.recipe, name='recipe/'),
    path('buchi/', views.buchii, name='buchi/'),
    path('buchi1/', views.buchii1, name='buchi1/'),
    path('buchi2/', views.buchii2, name='buchi2/'),
    path('bibingkaa/', views.bibingkaaa, name='bibingkaa/'),
    path('bibingka1/', views.bibingkaa1, name='bibingka1/'),
    path('bibingka2/', views.bibingkaa2, name='bibingka2/'),
    path('sansrival/', views.sansrivalll, name='sansrival/'),
    path('sansrival1/', views.sansrivalll1, name='sansrival1/'),
    path('sansrival2/', views.sansrivalll2, name='sansrival2/'),
    path('pichii/', views.pichiiii, name='pichii/'),
    path('pichi1/', views.pichiii1, name='pichi1/'),
    path('pichi2/', views.pichiii2, name='pichi2/'),
    path('putoo/', views.putooo, name='putoo/'),
    path('puto1/', views.putooo1, name='puto1/'),
    path('puto2/', views.putooo2, name='puto2/'),
    path('tahoo/', views.tahooo, name='tahoo/'),
    path('taho1/', views.tahooo1, name='taho1/'),
    path('taho2/', views.tahooo2, name='taho2/'),
    path('turonn/', views.turonnn, name='turonn/'),
    path('turon1/', views.turonnn1, name='turon1/'),
    path('turon2/', views.turonnn2, name='turon2/'),
    path('bananacuee/', views.bananaaa, name='bananacuee/'),
    path('bananacuee1/', views.bananaaa1, name='bananacuee1/'),
    path('bananacuee2/', views.bananaaa2, name='bananacuee2/'),
    path('halohaloo/', views.halohalooo, name='halohaloo/'),
    path('halohaloo1/', views.halohalooo1, name='halohaloo1/'),
    path('halohaloo2/', views.halohalooo2, name='halohaloo2/'),
    path('lecheflann/', views.lecheflannn, name='lecheflann/'),
    path('lecheflann1/', views.lecheflannn1, name='lecheflann1/'),
    path('lecheflann2/', views.lecheflannn2, name='lecheflann2/'),
    path('aboutUs/', views.aboutUs, name='aboutUs/'),
    path('index/', views.personalInfoForm, name='index'),

    url(r'^index2/(\d+)/$', views.dessertInfoForm, name = 'dessertInfoForm'),

    url(r'^index3/(\d+)/(\d+)/$', views.ingredients, name = 'ingredients'),

    url(r'^index4/(\d+)/(\d+)/(\d+)/$', views.directiontoCookForm, name = 'directiontoCookForm'),

    url(r'^tableshowform/(\d+)/$', views.tableShowForm, name = 'tableshowform'),

    url(r'^delete/(\d+)/(\d+)/$', views.delete, name = 'delete')
]