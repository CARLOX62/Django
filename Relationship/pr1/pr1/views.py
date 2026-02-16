from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world")
    return render(request, "website/index.html")

def about(request):
    # return HttpResponse("Hey, My Name is Aniket")
    return render(request, "website/about.html")

def contact(request):
    # return HttpResponse("How Are You?")
    return render(request, "website/contact.html")
