
"""
URL configuration for Travels project.

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
from django.urls import path
from Tharun import views

app_name = 'Tharun'
urlpatterns = [
    path('city-guides', views.cityguide, name='cityguides'),
    path('services', views.service, name='services'),
    path('travel', views.travel, name='travel'),
    path('contact', views.contact, name='contact'),
    path('onepage', views.onepage, name='onepage'),
    path('login_reg', views.login, name='login_reg'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),

    path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart '),
   
]
