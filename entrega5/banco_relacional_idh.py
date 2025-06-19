from federacao import Federacao
from federacao_dao_postgres import FederacaoDAOPostgres

def inserir_federacoes(nome_arquivo):
    dao = FederacaoDAOPostgres()
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            dados = [campo.strip() for campo in linha.strip().split(";")]
            if len(dados) == 7:
                fed = Federacao(*dados)
                dao.incluir_federacao(fed)
            else:
                print("Linha ignorada (inválida):", linha)
    dao.fecha_conexao()

if __name__ == "__main__":
    inserir_federacoes("/home/fernanda/Projects/nosql/entrega5/idh.txt")
