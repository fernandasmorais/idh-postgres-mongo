import psycopg2

from piloto import PilotoDAO
import matplotlib.pyplot as plt


class PilotoDAO:
    def __init__(self):
        self.con = psycopg2.connect(
            host="localhost", database="postgres", user="postgres", password="postgres"
        )
        self.cursor = self.con.cursor()
        print("Conectado ao PostgreSQL!")

    def fechaConexao(self):
        self.cursor.close()
        self.con.close()
        print("Conexão ao PostgreSQL foi encerrada")

    def incluirPiloto(self, piloto):
        sql = "INSERT INTO piloto (id, ano_campeonato, nacionalidade, nome_piloto, equipe) VALUES (%s, %s, %s, %s, %s)"
        valores = (
            piloto.id,
            piloto.ano_campeonato,
            piloto.nacionalidade,
            piloto.nome_piloto,
            piloto.equipe,
        )
        self.cursor.execute(sql, valores)
        self.con.commit()
        print(f"Piloto {piloto.nome_piloto} inserido com sucesso!")


def inserir_pilotos_do_arquivo(nome_arquivo):
    dao = PilotoDAO()
    with open(nome_arquivo, "r") as arquivo:
        id_counter = 1
        for linha in arquivo:
            dados = [campo.strip() for campo in linha.strip().split(";")]
            print("Lendo linha:", dados)
            if len(dados) == 4:
                piloto = PilotoDAO()
                piloto.id = id_counter
                piloto.ano_campeonato = int(dados[0])
                piloto.nacionalidade = dados[1]
                piloto.nome_piloto = dados[2]
                piloto.equipe = dados[3]
                print(f"Inserindo piloto: {piloto.nome_piloto}")
                dao.incluirPiloto(piloto)
                id_counter += 1
            else:
                print("Linha ignorada (formato inválido):", linha)
    dao.fechaConexao()
    print("Todos os pilotos do arquivo foram inseridos!")


if __name__ == "__main__":
    inserir_pilotos_do_arquivo("/home/fernanda/Projects/nosql/formula1.txt")
