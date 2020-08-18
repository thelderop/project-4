from django.shortcuts import render
from .models import State, Senator, Senate_Bill

# Create your views here.
def state_detail_view(request):
    obj = State.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "state/detail.html", context)

def senator_detail_view(request):
    return render(request, "senator/detail.html", {})

def senate_bill_detail_view(request):
    return render(request, "senate_bill/detail.html", {})