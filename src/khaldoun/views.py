from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def buildwithai(request):
    return render(request, "buildwithai.html")
