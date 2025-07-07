from django.db import models

# RF03 - Cidade
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

# RF02 - Tipo de Pessoa
class TipoPessoa(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Tipo (física ou jurídica)")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Pessoa"
        verbose_name_plural = "Tipos de Pessoas"

# RF05 - Ocupação
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

# RF06 - Área de Contratação
class AreaContratacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área de Contratação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área de Contratação"
        verbose_name_plural = "Áreas de Contratação"

# RF01 - Pessoa
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(max_length=100, verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ocupação")
    area_contratacao = models.ForeignKey(AreaContratacao, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Área de Interesse")
    tipo_pessoa = models.ForeignKey(TipoPessoa, on_delete=models.SET_NULL, null=True, verbose_name="Tipo de Pessoa")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

# RF04 - Currículo
class Curriculo(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa")
    link_curriculo = models.URLField(max_length=200, verbose_name="Link do Currículo (Lattes)")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, verbose_name="Ocupação Relacionada")
    resumo = models.TextField(verbose_name="Resumo Profissional")
    formacao = models.TextField(verbose_name="Formação Acadêmica")
    experiencias = models.TextField(verbose_name="Experiências Profissionais")
    habilidades = models.TextField(verbose_name="Habilidades")

    def __str__(self):
        return f"Currículo de {self.pessoa.nome}"

    class Meta:
        verbose_name = "Currículo"
        verbose_name_plural = "Currículos"

class Empresa(models.Model):
    nome_razao = models.CharField(max_length=100, verbose_name="Razão Social")
    nome_fantasia = models.CharField(max_length=100, verbose_name="Nome Fantasia")
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(max_length=100, verbose_name="Email")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    tipo_pessoa = models.ForeignKey(TipoPessoa, on_delete=models.SET_NULL, null=True, verbose_name="Tipo de Pessoa")

    def __str__(self):
        return self.nome_fantasia

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

# RF07 - Vaga
class Vaga(models.Model):
    EMPREGO = 'Emprego'
    ESTAGIO = 'Estágio'
    TIPO_VAGA_CHOICES = [
        (EMPREGO, 'Emprego'),
        (ESTAGIO, 'Estágio'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome da vaga")
    descricao = models.TextField(verbose_name="Descrição da vaga")
    requisitos = models.TextField(verbose_name="Requisitos da vaga")
    tipo = models.CharField(max_length=10, choices=TIPO_VAGA_CHOICES, verbose_name="Tipo da vaga")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, limit_choices_to={'tipo_pessoa__nome': 'Pessoa Jurídica'}, verbose_name="Empresa")
    area_contratacao = models.ForeignKey(AreaContratacao, on_delete=models.SET_NULL, null=True, verbose_name="Área de Contratação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Vaga"
        verbose_name_plural = "Vagas"

# RF08 - Candidatura
class Candidatura(models.Model):
    PENDENTE = 'Pendente'
    ACEITA = 'Aceita'
    RECUSADA = 'Recusada'
    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (ACEITA, 'Aceita'),
        (RECUSADA, 'Recusada'),
    ]

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Candidato")
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, verbose_name="Vaga")
    data_candidatura = models.DateField(auto_now_add=True, verbose_name="Data da candidatura")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDENTE, verbose_name="Status")

    def __str__(self):
        return f"{self.pessoa.nome} - {self.vaga.nome}"

    class Meta:
        verbose_name = "Candidatura"
        verbose_name_plural = "Candidaturas"



