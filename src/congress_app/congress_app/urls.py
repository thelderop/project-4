"""congress_app URL Configuration

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

from pages.views import home_view, state_view, senator_view, bill_view
from congress.views import state_detail_view, senate_bill_detail_view, senator_detail_view, state_create_view, senator_create_view, senate_bill_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path ('search-state/', state_view, name="state"),
    path ('search-bill/', bill_view, name="bill"),
    path ('search-senator/', senator_view, name="senator"),
    path ('detail-state/', state_detail_view),
    path ('detail-senator/', senator_detail_view),
    path ('detail-senate_bill/', senate_bill_detail_view),
    path ('create-state/', state_create_view),
    path ('create-senator/', senator_create_view),
    path ('create-senate_bill/', senate_bill_create_view)
]
