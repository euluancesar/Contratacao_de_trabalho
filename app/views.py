from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        # Aqui você pode tratar dados de formulários, se houver
        pass

# Exemplo 1: Buscar vagas
# def post(self, request, *args, **kwargs):
#     termo = request.POST.get('busca')
#     vagas = Vaga.objects.filter(nome__icontains=termo)
#     return render(request, 'index.html', {'vagas': vagas, 'busca': termo})
    

# Exemplo 2: Redirecionar para login ou cadastro
# def post(self, request, *args, **kwargs):
#     if 'entrar' in request.POST:
#         return redirect('login')
#     elif 'cadastrar' in request.POST:
#         return redirect('cadastro')
#     return render(request, 'index.html')
    



# app/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cidade, TipoPessoa, Ocupacao, AreaContratacao, Pessoa, Curriculo, Empresa, Vaga, Candidatura
from .forms import *

class CidadeListView(ListView):
    model = Cidade
    template_name = 'cidade_list.html'
    context_object_name = 'cidades'

class CidadeCreateView(CreateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cidade_list.html'
    success_url = reverse_lazy('cidade_list')
    extra_context = {'form_title': 'Cadastrar Cidade'}

class CidadeUpdateView(UpdateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cidade_list.html'
    success_url = reverse_lazy('cidade_list')
    extra_context = {'form_title': 'Editar Cidade'}

class CidadeDeleteView(DeleteView):
    model = Cidade
    template_name = 'cidade_list.html'
    success_url = reverse_lazy('cidade_list')

# Repita o mesmo padrão para as demais views:

class TipoPessoaListView(ListView):
    model = TipoPessoa
    template_name = 'tipopessoa_list.html'
    context_object_name = 'tipos'

class TipoPessoaCreateView(CreateView):
    model = TipoPessoa
    form_class = TipoPessoaForm
    template_name = 'tipopessoa_list.html'
    success_url = reverse_lazy('tipopessoa_list')
    extra_context = {'form_title': 'Cadastrar Tipo de Pessoa'}

class TipoPessoaUpdateView(UpdateView):
    model = TipoPessoa
    form_class = TipoPessoaForm
    template_name = 'tipopessoa_list.html'
    success_url = reverse_lazy('tipopessoa_list')
    extra_context = {'form_title': 'Editar Tipo de Pessoa'}

class TipoPessoaDeleteView(DeleteView):
    model = TipoPessoa
    template_name = 'tipopessoa_list.html'
    success_url = reverse_lazy('tipopessoa_list')



class PessoaListView(ListView):
    model = Pessoa
    template_name = 'pessoa_list.html'
    context_object_name = 'pessoas'

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'pessoa_list.html'
    success_url = reverse_lazy('pessoa_list')
    extra_context = {'form_title': 'Cadastrar Pessoa'}

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'pessoa_list.html'
    success_url = reverse_lazy('pessoa_list')
    extra_context = {'form_title': 'Editar Pessoa'}

class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = 'pessoa_list.html'
    success_url = reverse_lazy('pessoa_list')






class OcupacaoListView(ListView):
    model = Ocupacao
    template_name = 'ocupacao_list.html'
    context_object_name = 'ocupacoes'

class OcupacaoCreateView(CreateView):
    model = Ocupacao
    form_class = OcupacaoForm
    template_name = 'ocupacao_list.html'
    success_url = reverse_lazy('ocupacao_list')
    extra_context = {'form_title': 'Cadastrar Ocupação'}

class OcupacaoUpdateView(UpdateView):
    model = Ocupacao
    form_class = OcupacaoForm
    template_name = 'ocupacao_list.html'
    success_url = reverse_lazy('ocupacao_list')
    extra_context = {'form_title': 'Editar Ocupação'}

class OcupacaoDeleteView(DeleteView):
    model = Ocupacao
    template_name = 'ocupacao_list.html'
    success_url = reverse_lazy('ocupacao_list')

class AreaContratacaoListView(ListView):
    model = AreaContratacao
    template_name = 'areacontratacao_list.html'
    context_object_name = 'areas'

class AreaContratacaoCreateView(CreateView):
    model = AreaContratacao
    form_class = AreaContratacaoForm
    template_name = 'areacontratacao_list.html'
    success_url = reverse_lazy('areacontratacao_list')
    extra_context = {'form_title': 'Cadastrar Área de Contratação'}

class AreaContratacaoUpdateView(UpdateView):
    model = AreaContratacao
    form_class = AreaContratacaoForm
    template_name = 'areacontratacao_list.html'
    success_url = reverse_lazy('areacontratacao_list')
    extra_context = {'form_title': 'Editar Área de Contratação'}

class AreaContratacaoDeleteView(DeleteView):
    model = AreaContratacao
    template_name = 'areacontratacao_list.html'
    success_url = reverse_lazy('areacontratacao_list')

class CurriculoListView(ListView):
    model = Curriculo
    template_name = 'curriculo_list.html'
    context_object_name = 'curriculos'

class CurriculoCreateView(CreateView):
    model = Curriculo
    form_class = CurriculoForm
    template_name = 'curriculo_list.html'
    success_url = reverse_lazy('curriculo_list')
    extra_context = {'form_title': 'Cadastrar Currículo'}

class CurriculoUpdateView(UpdateView):
    model = Curriculo
    form_class = CurriculoForm
    template_name = 'curriculo_list.html'
    success_url = reverse_lazy('curriculo_list')
    extra_context = {'form_title': 'Editar Currículo'}

class CurriculoDeleteView(DeleteView):
    model = Curriculo
    template_name = 'curriculo_list.html'
    success_url = reverse_lazy('curriculo_list')

class EmpresaListView(ListView):
    model = Empresa
    template_name = 'empresa_list.html'
    context_object_name = 'empresas'

class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa_list.html'
    success_url = reverse_lazy('empresa_list')
    extra_context = {'form_title': 'Cadastrar Empresa'}

class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa_list.html'
    success_url = reverse_lazy('empresa_list')
    extra_context = {'form_title': 'Editar Empresa'}

class EmpresaDeleteView(DeleteView):
    model = Empresa
    template_name = 'empresa_list.html'
    success_url = reverse_lazy('empresa_list')

class VagaListView(ListView):
    model = Vaga
    template_name = 'vaga_list.html'
    context_object_name = 'vagas'

class VagaCreateView(CreateView):
    model = Vaga
    form_class = VagaForm
    template_name = 'vaga_list.html'
    success_url = reverse_lazy('vaga_list')
    extra_context = {'form_title': 'Cadastrar Vaga'}

class VagaUpdateView(UpdateView):
    model = Vaga
    form_class = VagaForm
    template_name = 'vaga_list.html'
    success_url = reverse_lazy('vaga_list')
    extra_context = {'form_title': 'Editar Vaga'}

class VagaDeleteView(DeleteView):
    model = Vaga
    template_name = 'vaga_list.html'
    success_url = reverse_lazy('vaga_list')

class CandidaturaListView(ListView):
    model = Candidatura
    template_name = 'candidatura_list.html'
    context_object_name = 'candidaturas'

class CandidaturaCreateView(CreateView):
    model = Candidatura
    form_class = CandidaturaForm
    template_name = 'candidatura_list.html'
    success_url = reverse_lazy('candidatura_list')
    extra_context = {'form_title': 'Cadastrar Candidatura'}

class CandidaturaUpdateView(UpdateView):
    model = Candidatura
    form_class = CandidaturaForm
    template_name = 'candidatura_list.html'
    success_url = reverse_lazy('candidatura_list')
    extra_context = {'form_title': 'Editar Candidatura'}

class CandidaturaDeleteView(DeleteView):
    model = Candidatura
    template_name = 'candidatura_list.html'
    success_url = reverse_lazy('candidatura_list')

