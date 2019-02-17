"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from shop101.views import test
from shop101.views import product,expand,expand1,expand2,expand3,show_product

urlpatterns = [
    path('test/',test),
    path('product/',product),
    path('admin/', admin.site.urls),
    # path('product/first',expand),
    # path('product/second',expand1),
    # path('product/third',expand2),
    # path('product/fourth',expand3)
    path('product/product/<id>',show_product),
    path('user/', include('django.contrib.auth.urls')),
]
    