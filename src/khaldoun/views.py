from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def imprint(request):
    return render(request, "imprint.html")


def gild(request):
    return render(request, "gild.html")
