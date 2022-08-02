from django.shortcuts import render

# Create your views here.
def inicio (request):
    saludo = 'holaaaaaaa'
    return render(request, 'inicio.html', saludo)