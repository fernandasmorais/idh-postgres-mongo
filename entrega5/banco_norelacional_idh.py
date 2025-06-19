from federacao import Federacao
from pymongo import MongoClient

def inserir_federacoes_mongo(caminho_csv):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["idh_database"]
    colecao = db["federacoes"]

    with open(caminho_csv, "r") as arquivo:
        for linha in arquivo:
            dados = [campo.strip() for campo in linha.strip().split(";")]
            if len(dados) == 7:
                fed = Federacao(*dados)
                doc = {
                    "ano": fed.ano,
                    "codigo_federacao": fed.codigo_federacao,
                    "nome_federacao": fed.nome_federacao,
                    "cod_municipio": fed.cod_municipio,
                    "municipio": fed.municipio,
                    "esperanca_vida": fed.esperanca_vida,
                    "mortalidade_infantil": fed.mortalidade_infantil
                }
                colecao.insert_one(doc)
                print(f"Inserido no MongoDB: {fed.nome_federacao}")
            else:
                print("Linha ignorada (inválida):", linha)

    client.close()
    print("Conexão MongoDB encerrada.")

if __name__ == "__main__":
    inserir_federacoes_mongo("/home/fernanda/Projects/nosql/entrega5/idh.txt")
