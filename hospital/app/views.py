from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request,'index.html')


def login(request):
    return render(request,'login.html')

def citas(request):
    return render(request,'citas.html')

def contacto(request):
    return render(request,'contacto.html')