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

def pagina3 (request):
    from .models import pessoa
    dicionario = {}
    registros = pessoa.objects.all()
    dicionario['pessoas'] = registros
    return render(request, 'pagina3.html', dicionario)


from django.views.generic import ListView
from .models import pessoa
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
class pessoa_create(CreateView):
    from .models import pessoa
    model = pessoa
    fields = ['nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']
    def get_sucess_url(self):
        return reverse_lazy('pagina3.html')