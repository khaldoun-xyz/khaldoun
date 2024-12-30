
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def growth(request):
    return render(request, "growth.html")

