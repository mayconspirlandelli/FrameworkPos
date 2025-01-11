from django.shortcuts import render 
from django.http import HttpResponse 

from django.contrib.auth import authenticate, login, logout
def index(request):
    print("else")
    usuario = request.POST.get('username')
    senha = request.POST.get('password')
    user = authenticate(username=usuario, password=senha)
    if (user is not None):
        login(request, user)
        request.session['username'] = usuario
        request.session['password'] = senha
        request.session['usernamefull'] = user.get_full_name()
        print(request.session['username'])
        print(request.session['password'])
        print(request.session['usernamefull'])
        from django.shortcuts import redirect
        return redirect('menu_alias')
    else:
        return render(request, 'index.html')

from django_tables2 import SingleTableView
class pessoa_menu(SingleTableView):
    from .models import pessoa
    from .tables import pessoa_table
    model = pessoa 
    tables_class = pessoa_table
    template_name_suffix = '_menu'
    table_pagination = {"per_page": 5}
    template_name = 'exemplo01/pessoa_menu.html'


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


from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import pessoa
class pessoa_create(CreateView):
    model = pessoa
    fields = ['nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']
    def get_sucess_url(self):
        return reverse_lazy('pessoa_create')


from django.views.generic import ListView
class pessoa_list(ListView):
    from .models import pessoa
    model = pessoa
    #Exibe apenas registros ativos.
    #queryset = pessoa.objects.filter(ativo=True)


from django.views.generic.edit import UpdateView
class pessoa_update(UpdateView):
    from .models import pessoa
    model = pessoa
    fields =[ 'nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']
    def get_sucess_url(self):
        return reverse_laz('pessoa_list_alias')


from django.views.generic.edit import DeleteView
class pessoa_delete(DeleteView):
    from .models import pessoa 
    model = pessoa        
    fields =[ 'nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']
    template_name_suffix = '_delete'
    def get_sucess_url(self):
        return reverse_lazy('pessoa_list_alias')


def pagina4 (request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    celular = request.POST.get('celular')
    funcao = request.POST.get('funcao')
    nascimento = request.POST.get('nascimento')
    ativo = request.POST.get('ativo')

    print("Nome:", nome)
    print("email:", email)
    print("Celular:", celular)
    print("Função:", funcao)
    print("Nascimento:", nascimento)
    print("Ativo:", ativo)
    
    return render(request, 'pagina4.html')
