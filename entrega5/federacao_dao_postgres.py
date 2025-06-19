import psycopg2

class FederacaoDAOPostgres:
    def __init__(self):
        self.con = psycopg2.connect(
            host="localhost", database="postgres", user="postgres", password="postgres"
        )
        self.cursor = self.con.cursor()
        print("Conectado ao PostgreSQL!")

    def fecha_conexao(self):
        self.cursor.close()
        self.con.close()
        print("Conexão encerrada.")

    def incluir_federacao(self, federacao):
        sql = """
            INSERT INTO federacao 
            (ano, codigo_federacao, nome_federacao, cod_municipio, municipio, esperanca_vida, mortalidade_infantil)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            federacao.ano,
            federacao.codigo_federacao,
            federacao.nome_federacao,
            federacao.cod_municipio,
            federacao.municipio,
            federacao.esperanca_vida,
            federacao.mortalidade_infantil
        )
        self.cursor.execute(sql, valores)
        self.con.commit()
        print(f"Inserido: {federacao.nome_federacao}")
