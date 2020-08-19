from django.shortcuts import render
from .models import State, Senator, Senate_Bill
from .forms import StateForm, SenatorForm, Senate_BillForm

# State views
def state_detail_view(request):
    obj = State.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "state/detail.html", context)

def state_create_view(request):
    form = StateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "state/create.html", context)

# Senator views
def senator_detail_view(request):
    obj = Senator.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "senator/detail.html", context)

def senator_create_view(request):
    form = SenatorForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "senator/create.html", context)

# Senate_Bill views
def senate_bill_detail_view(request):
    obj = Senate_Bill.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "senate_bill/detail.html", context)

def senate_bill_create_view(request):
    form = Senate_BillForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "senate_bill/create.html", context)