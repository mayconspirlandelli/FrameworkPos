from django.shortcuts import render 
from django.http import HttpResponse 

def index (request):
    return HttpResponse ("EXEMPLO 01.")

def pagina0 (request):
    return render(request, 'pagina0.html')    

def pagina1 (request):
    return render(request, 'pagina1.html')

def pagina2 (request):
    from .models import pessoa
    dicionario = {}
    registros = pessoa.objects.all()
    dicionario['pessoas'] = registros 
    return render(request, 'pagina2.html', dicionario)