from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def services(request):
    return render(request, 'mainapp/services.html')

def dialysis(request):
        return render(request, 'mainapp/dialysis.html')

def dental(request):
    return render(request, 'mainapp/dental.html')

def physiotherapy(request):
    return render(request, 'mainapp/physiotherapy.html')

def nutrition(request):
    return render(request, 'mainapp/nutrition.html')

def diagnostic(request):
    return render(request, 'mainapp/diagnostic.html')