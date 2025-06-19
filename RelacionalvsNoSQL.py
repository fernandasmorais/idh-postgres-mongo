import psycopg2
from pymongo import MongoClient

class Piloto:
    def __init__(self):
        self.id = 0
        self.ano_campeonato = 0
        self.nacionalidade = ""
        self.nome_piloto = ""
        self.equipe = ""

class Conecta:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="aula_puc", collection_name="piloto"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def incluir(self, documento):
        resultado = self.collection.insert_one(documento)
        print(f"Documento inserido com _id: {resultado.inserted_id}")

    def abreConexao(self):
        try:
            self.con = psycopg2.connect(
                host="localhost", database="postgres", user="postgres", password="postgres"
            )
            self.cursor = self.con.cursor()
            self.cursor.execute('SELECT version();')
            db_info = self.cursor.fetchone()
            print("Conectado ao PostgreSQL - versão:", db_info[0])
        except Exception as e:
            print("Erro ao conectar:", e)

    def fechaConexao(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.con:
                self.con.close()
            print("Conexão ao PostgreSQL foi encerrada")
        except Exception as e:
            print("Erro ao fechar conexão:", e)

    def le_banco(self):
        sql = "SELECT * FROM piloto"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        lista_piloto = []
        for linha in result:
            piloto = Piloto()
            piloto.id = int(linha[0])
            piloto.ano_campeonato = linha[1]
            piloto.nacionalidade = linha[2]
            piloto.nome_piloto = linha[4]
            piloto.equipe = linha[3]
            lista_piloto.append(piloto)
        return lista_piloto

if __name__ == "__main__":
    print("oi")
    conecta = Conecta()
    conecta.abreConexao()
    lista = conecta.le_banco()
    conecta.fechaConexao()
    for p in lista:
        novo_doc = {"ano_campeonato": p.ano_campeonato, "nacionalidade":p.nacionalidade, "nome_piloto": p.nome_piloto, "equipe": p.equipe}
        conecta.incluir(novo_doc)
