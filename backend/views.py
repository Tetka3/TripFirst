from django.shortcuts import render
from .models import Trip 

# Create your views here.

def index(request):
    context = {
        'trips': Trip.objects.all()
    }
    return render(request, 'trips/index.html', context)