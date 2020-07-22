from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "app/index.html")


def about(request):
    return render(request, "app/about.html")


def contact(request):
    return render(request, "app/contact.html")


def store(request):
    return render(request, "app/store.html")