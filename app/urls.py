# app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('cidade/', CidadeListCreateView.as_view(), name='cidade_list'),
    path('cidade/create/', CidadeListCreateView.as_view(), name='cidade_create'),
    path('cidade/update/<int:pk>/', CidadeUpdateView.as_view(), name='cidade_update'),
    path('cidade/delete/<int:pk>/', CidadeDeleteView.as_view(), name='cidade_delete'),

    path('tipopessoa/', TipoPessoaListView.as_view(), name='tipopessoa_list'),
    path('tipopessoa/create/', TipoPessoaCreateView.as_view(), name='tipopessoa_create'),
    path('tipopessoa/update/<int:pk>/', TipoPessoaUpdateView.as_view(), name='tipopessoa_update'),
    path('tipopessoa/delete/<int:pk>/', TipoPessoaDeleteView.as_view(), name='tipopessoa_delete'),

    path('ocupacao/', OcupacaoListCreateView.as_view(), name='ocupacao_list'),
    path('ocupacao/create/', OcupacaoListCreateView.as_view(), name='ocupacao_create'),
    path('ocupacao/update/<int:pk>/', OcupacaoUpdateView.as_view(), name='ocupacao_update'),
    path('ocupacao/delete/<int:pk>/', OcupacaoDeleteView.as_view(), name='ocupacao_delete'),

    path('areacontratacao/', AreaContratacaoListCreateView.as_view(), name='areacontratacao_list'),
    path('areacontratacao/create/', AreaContratacaoListCreateView.as_view(), name='areacontratacao_create'),
    path('areacontratacao/update/<int:pk>/', AreaContratacaoUpdateView.as_view(), name='areacontratacao_update'),
    path('areacontratacao/delete/<int:pk>/', AreaContratacaoDeleteView.as_view(), name='areacontratacao_delete'),

    path('pessoa/', PessoaListCreateView.as_view(), name='pessoa_list'),
    path('pessoa/create/', PessoaListCreateView.as_view(), name='pessoa_create'),
    path('pessoa/update/<int:pk>/', PessoaUpdateView.as_view(), name='pessoa_update'),
    path('pessoa/delete/<int:pk>/', PessoaDeleteView.as_view(), name='pessoa_delete'),

    path('curriculo/', CurriculoListCreateView.as_view(), name='curriculo_list'),
    path('curriculo/create/', CurriculoListCreateView.as_view(), name='curriculo_create'),
    path('curriculo/update/<int:pk>/', CurriculoUpdateView.as_view(), name='curriculo_update'),
    path('curriculo/delete/<int:pk>/', CurriculoDeleteView.as_view(), name='curriculo_delete'),

    path('empresa/', EmpresaListCreateView.as_view(), name='empresa_list'),
    path('empresa/criar/', EmpresaListCreateView.as_view(), name='empresa_create'),
    path('empresa/<int:pk>/editar/', EmpresaUpdateView.as_view(), name='empresa_update'),
    path('empresa/<int:pk>/excluir/', EmpresaDeleteView.as_view(), name='empresa_delete'),

    path('vaga/', VagaListCreateView.as_view(), name='vaga_list'),
    path('vaga/create/', VagaListCreateView.as_view(), name='vaga_create'),
    path('vaga/update/<int:pk>/', VagaUpdateView.as_view(), name='vaga_update'),
    path('vaga/delete/<int:pk>/', VagaDeleteView.as_view(), name='vaga_delete'),

    path('candidatura/', CandidaturaListCreateView.as_view(), name='candidatura_list'),
    path('candidatura/create/', CandidaturaListCreateView.as_view(), name='candidatura_create'),
    path('candidatura/update/<int:pk>/', CandidaturaUpdateView.as_view(), name='candidatura_update'),
    path('candidatura/delete/<int:pk>/', CandidaturaDeleteView.as_view(), name='candidatura_delete'),
]