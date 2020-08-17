from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def state_view(request, *args, **kwargs):
    return render(request, "search-state.html", {})

def senator_view(request, *args, **kwargs):
    return render(request, "search-senator.html", {})

def bill_view(request, *args, **kwargs):
    return render(request, "search-bill.html", {})