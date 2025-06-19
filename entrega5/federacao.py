class Federacao:
    def __init__(self, ano, codigo_federacao, nome_federacao, cod_municipio, municipio, esperanca_vida, mortalidade_infantil):
        self.ano = int(ano)
        self.codigo_federacao = codigo_federacao
        self.nome_federacao = nome_federacao
        self.cod_municipio = cod_municipio
        self.municipio = municipio

        ## resolvendo casos de esperança de vida
        self.esperanca_vida = float(esperanca_vida.replace(",", ".").replace(" ", ""))
        self.mortalidade_infantil = float(mortalidade_infantil.replace(",", ".").replace(" ", ""))
