from django import forms
from .models import Cidade, TipoPessoa, Ocupacao, AreaContratacao, Pessoa, Curriculo, Empresa, Vaga, Candidatura
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'

class TipoPessoaForm(forms.ModelForm):
    class Meta:
        model = TipoPessoa
        fields = '__all__'

class OcupacaoForm(forms.ModelForm):
    class Meta:
        model = Ocupacao
        fields = '__all__'

class AreaContratacaoForm(forms.ModelForm):
    class Meta:
        model = AreaContratacao
        fields = '__all__'

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class CurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = '__all__'

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_fantasia', 'cnpj', 'email', 'telefone', 'cidade', 'tipo_pessoa']

    def __init__(self, *args, **kwargs):
        super(EmpresaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome_fantasia',
            'cnpj',
            'email',
            'telefone',
            'cidade',
            'tipo_pessoa',
            Submit('submit', 'Salvar')
        )

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = '__all__'

class CandidaturaForm(forms.ModelForm):
    class Meta:
        model = Candidatura
        fields = '__all__'