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

# class CidadeListView(ListView):
#     model = Cidade
#     template_name = 'cidade_list.html'
#     context_object_name = 'cidades'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = CidadeForm()  # <-- Isso resolve tudo
#         return context

# class CidadeCreateView(CreateView):
#     model = Cidade
#     form_class = CidadeForm
#     template_name = 'cidade_list.html'
#     success_url = reverse_lazy('cidade_list')
#     extra_context = {'form_title': 'Cadastrar Cidade'}

# class CidadeUpdateView(UpdateView):
#     model = Cidade
#     form_class = CidadeForm
#     template_name = 'cidade_list.html'
#     success_url = reverse_lazy('cidade_list')
#     extra_context = {'form_title': 'Editar Cidade'}

# class CidadeDeleteView(DeleteView):
#     model = Cidade
#     template_name = 'cidade_list.html'
#     success_url = reverse_lazy('cidade_list')

# Repita o mesmo padrão para as demais views:


class CidadeListCreateView(View):
    template_name = 'cidade_list.html'

    def get(self, request):
        cidades = Cidade.objects.all()
        form = CidadeForm()
        return render(request, self.template_name, {'cidades': cidades, 'form': form, 'form_title': 'Cadastrar Cidade'})

    def post(self, request):
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cidade_list')
        cidades = Cidade.objects.all()
        return render(request, self.template_name, {'cidades': cidades, 'form': form, 'form_title': 'Cadastrar Cidade'})

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




class TipoPessoaListView(ListView):
    model = TipoPessoa
    template_name = 'tipopessoa_list.html'
    context_object_name = 'tipos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TipoPessoaForm()  # <-- Isso resolve tudo
        return context

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



# class PessoaListView(ListView):
#     model = Pessoa
#     template_name = 'pessoa_list.html'
#     context_object_name = 'pessoas'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = PessoaForm()  # <-- Isso resolve tudo
#         return context

# class PessoaCreateView(CreateView):
#     model = Pessoa
#     form_class = PessoaForm
#     template_name = 'pessoa_list.html'
#     success_url = reverse_lazy('pessoa_list')
#     extra_context = {'form_title': 'Cadastrar Pessoa'}

# class PessoaUpdateView(UpdateView):
#     model = Pessoa
#     form_class = PessoaForm
#     template_name = 'pessoa_list.html'
#     success_url = reverse_lazy('pessoa_list')
#     extra_context = {'form_title': 'Editar Pessoa'}

# class PessoaDeleteView(DeleteView):
#     model = Pessoa
#     template_name = 'pessoa_list.html'
#     success_url = reverse_lazy('pessoa_list')
    


class PessoaListCreateView(View):
    template_name = 'pessoa_list.html'

    def get(self, request):
        pessoas = Pessoa.objects.all()
        form = PessoaForm()
        return render(request, self.template_name, {'pessoas': pessoas, 'form': form, 'form_title': 'Cadastrar Pessoa'})

    def post(self, request):
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pessoa_list')
        pessoas = Pessoa.objects.all()
        return render(request, self.template_name, {'pessoas': pessoas, 'form': form, 'form_title': 'Cadastrar Pessoa'})

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







# class OcupacaoListView(ListView):
#     model = Ocupacao
#     template_name = 'ocupacao_list.html'
#     context_object_name = 'ocupacoes'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = OcupacaoForm()  # <-- Isso resolve tudo
#         return context

# class OcupacaoCreateView(CreateView):
#     model = Ocupacao
#     form_class = OcupacaoForm
#     template_name = 'ocupacao_list.html'
#     success_url = reverse_lazy('ocupacao_list')
#     extra_context = {'form_title': 'Cadastrar Ocupação'}

# class OcupacaoUpdateView(UpdateView):
#     model = Ocupacao
#     form_class = OcupacaoForm
#     template_name = 'ocupacao_list.html'
#     success_url = reverse_lazy('ocupacao_list')
#     extra_context = {'form_title': 'Editar Ocupação'}

# class OcupacaoDeleteView(DeleteView):
#     model = Ocupacao
#     template_name = 'ocupacao_list.html'
#     success_url = reverse_lazy('ocupacao_list')



class OcupacaoListCreateView(View):
    template_name = 'ocupacao_list.html'

    def get(self, request):
        ocupacoes = Ocupacao.objects.all()
        form = OcupacaoForm()
        return render(request, self.template_name, {'ocupacoes': ocupacoes, 'form': form, 'form_title': 'Cadastrar Ocupação'})

    def post(self, request):
        form = OcupacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ocupacao_list')
        ocupacoes = Ocupacao.objects.all()
        return render(request, self.template_name, {'ocupacoes': ocupacoes, 'form': form, 'form_title': 'Cadastrar Ocupação'})

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




# class AreaContratacaoListView(ListView):
#     model = AreaContratacao
#     template_name = 'areacontratacao_list.html'
#     context_object_name = 'areas'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = AreaContratacaoForm()  # <-- Isso resolve tudo
#         return context

# class AreaContratacaoCreateView(CreateView):
#     model = AreaContratacao
#     form_class = AreaContratacaoForm
#     template_name = 'areacontratacao_list.html'
#     success_url = reverse_lazy('areacontratacao_list')
#     extra_context = {'form_title': 'Cadastrar Área de Contratação'}

# class AreaContratacaoUpdateView(UpdateView):
#     model = AreaContratacao
#     form_class = AreaContratacaoForm
#     template_name = 'areacontratacao_list.html'
#     success_url = reverse_lazy('areacontratacao_list')
#     extra_context = {'form_title': 'Editar Área de Contratação'}

# class AreaContratacaoDeleteView(DeleteView):
#     model = AreaContratacao
#     template_name = 'areacontratacao_list.html'
#     success_url = reverse_lazy('areacontratacao_list')
    


class AreaContratacaoListCreateView(View):
    template_name = 'areacontratacao_list.html'

    def get(self, request):
        areas = AreaContratacao.objects.all()
        form = AreaContratacaoForm()
        return render(request, self.template_name, {'areas': areas, 'form': form, 'form_title': 'Cadastrar Área de Contratação'})

    def post(self, request):
        form = AreaContratacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('areacontratacao_list')
        areas = AreaContratacao.objects.all()
        return render(request, self.template_name, {'areas': areas, 'form': form, 'form_title': 'Cadastrar Área de Contratação'})

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





# class CurriculoListView(ListView):
#     model = Curriculo
#     template_name = 'curriculo_list.html'
#     context_object_name = 'curriculos'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = CurriculoForm()  # <-- Isso resolve tudo
#         return context

# class CurriculoCreateView(CreateView):
#     model = Curriculo
#     form_class = CurriculoForm
#     template_name = 'curriculo_list.html'
#     success_url = reverse_lazy('curriculo_list')
#     extra_context = {'form_title': 'Cadastrar Currículo'}

# class CurriculoUpdateView(UpdateView):
#     model = Curriculo
#     form_class = CurriculoForm
#     template_name = 'curriculo_list.html'
#     success_url = reverse_lazy('curriculo_list')
#     extra_context = {'form_title': 'Editar Currículo'}

# class CurriculoDeleteView(DeleteView):
#     model = Curriculo
#     template_name = 'curriculo_list.html'
#     success_url = reverse_lazy('curriculo_list')
    


class CurriculoListCreateView(View):
    template_name = 'curriculo_list.html'

    def get(self, request):
        curriculos = Curriculo.objects.all()
        form = CurriculoForm()
        return render(request, self.template_name, {'curriculos': curriculos, 'form': form, 'form_title': 'Cadastrar Currículo'})

    def post(self, request):
        form = CurriculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curriculo_list')
        curriculos = Curriculo.objects.all()
        return render(request, self.template_name, {'curriculos': curriculos, 'form': form, 'form_title': 'Cadastrar Currículo'})

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






# class EmpresaListView(ListView):
#     model = Empresa
#     template_name = 'empresa_list.html'
#     context_object_name = 'empresas'
#     def get(self, request):
#         form = EmpresaForm()
#         empresas = Empresa.objects.all()
#         return render(request, self.template_name, {
#             'form': form,
#             'empresas': empresas,
#         })

#     def post(self, request):
#         form = EmpresaForm(request.POST)
#         empresas = Empresa.objects.all()
#         print(form.is_valid())
#         if form.is_valid():
#             form.save()
#             return redirect('empresa_create')
#         return render(request, self.template_name, {
#             'form': form,
#             'empresas': empresas,
#         })

# class EmpresaCreateView(CreateView):
#     model = Empresa
#     form_class = EmpresaForm
#     template_name = 'empresa_list.html'
#     success_url = reverse_lazy('empresa_list')
#     extra_context = {'form_title': 'Cadastrar Empresa'}


    

# class EmpresaListCreateView(ListView, CreateView):
#     model = Empresa
#     form_class = EmpresaForm
#     template_name = 'empresa_list.html'
#     success_url = reverse_lazy('empresa_list')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['empresas'] = Empresa.objects.all()
#         context['form'] = self.get_form()
#         return context

#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             form.save()
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
    
class EmpresaListCreateView(View):
    template_name = 'empresa_list.html'

    def get(self, request):
        empresas = Empresa.objects.all()
        form = EmpresaForm()
        return render(request, self.template_name, {'empresas': empresas, 'form': form, 'form_title': 'Cadastrar Empresa'})

    def post(self, request):
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresa_list')  # Use o nome da sua URL
        empresas = Empresa.objects.all()
        return render(request, self.template_name, {'empresas': empresas, 'form': form, 'form_title': 'Cadastrar Empresa'})

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




# class VagaListView(ListView):
#     model = Vaga
#     template_name = 'vaga_list.html'
#     context_object_name = 'vagas'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = VagaForm()  # <-- Isso resolve tudo
#         return context

# class VagaCreateView(CreateView):
#     model = Vaga
#     form_class = VagaForm
#     template_name = 'vaga_list.html'
#     success_url = reverse_lazy('vaga_list')
#     extra_context = {'form_title': 'Cadastrar Vaga'}

# class VagaUpdateView(UpdateView):
#     model = Vaga
#     form_class = VagaForm
#     template_name = 'vaga_list.html'
#     success_url = reverse_lazy('vaga_list')
#     extra_context = {'form_title': 'Editar Vaga'}

# class VagaDeleteView(DeleteView):
#     model = Vaga
#     template_name = 'vaga_list.html'
#     success_url = reverse_lazy('vaga_list')





class VagaListCreateView(View):
    template_name = 'vaga_list.html'

    def get(self, request):
        vagas = Vaga.objects.all()
        form = VagaForm()
        return render(request, self.template_name, {'vagas': vagas, 'form': form, 'form_title': 'Cadastrar Vaga'})

    def post(self, request):
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaga_list')
        vagas = Vaga.objects.all()
        return render(request, self.template_name, {'vagas': vagas, 'form': form, 'form_title': 'Cadastrar Vaga'})

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






# class CandidaturaListView(ListView):
#     model = Candidatura
#     template_name = 'candidatura_list.html'
#     context_object_name = 'candidaturas'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = CandidaturaForm()  # <-- Isso resolve tudo
#         return context

# class CandidaturaCreateView(CreateView):
#     model = Candidatura
#     form_class = CandidaturaForm
#     template_name = 'candidatura_list.html'
#     success_url = reverse_lazy('candidatura_list')
#     extra_context = {'form_title': 'Cadastrar Candidatura'}

# class CandidaturaUpdateView(UpdateView):
#     model = Candidatura
#     form_class = CandidaturaForm
#     template_name = 'candidatura_list.html'
#     success_url = reverse_lazy('candidatura_list')
#     extra_context = {'form_title': 'Editar Candidatura'}

# class CandidaturaDeleteView(DeleteView):
#     model = Candidatura
#     template_name = 'candidatura_list.html'
#     success_url = reverse_lazy('candidatura_list')
    



class CandidaturaListCreateView(View):
    template_name = 'candidatura_list.html'

    def get(self, request):
        candidaturas = Candidatura.objects.all()
        form = CandidaturaForm()
        return render(request, self.template_name, {'candidaturas': candidaturas, 'form': form, 'form_title': 'Cadastrar Candidatura'})

    def post(self, request):
        form = CandidaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidatura_list')
        candidaturas = Candidatura.objects.all()
        return render(request, self.template_name, {'candidaturas': candidaturas, 'form': form, 'form_title': 'Cadastrar Candidatura'})

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


