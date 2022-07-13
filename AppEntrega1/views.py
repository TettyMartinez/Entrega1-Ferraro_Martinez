from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "AppEntrega1/inicio.html")

def atleta(request):
    return render(request, "AppEntrega1/atleta.html")

def coach(request):
    return render(request, "AppEntrega1/coach.html")

def club(request):
    return render(request, "AppEntrega1/club.html")