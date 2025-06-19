from banco.Piloto import Piloto
from banco.PilotoDAO import PilotoDAO
import matplotlib.pyplot as plt
 
def le_arquivo(nomeArquivo):
    campeoes = []
    arquivo = open(nomeArquivo + ".txt", "r")
    tamanho = arquivo.readlines()
    cont = 0
    p = Piloto()
    dao = PilotoDAO()
    while(len(tamanho) > cont):
        p = Piloto()
        linha = tamanho[cont]
        dados = linha.split(";")
        p.ano_campeonato = int(dados[0])
        p.nacionalidade = dados[1]
        p.nome_piloto = dados[2].strip()
        p.equipe = dados[3].strip()
        cont += 1  
        dao.incluirPiloto(p)
        campeoes.append(p)
    arquivo.close()
    dao.fechaConexao()
    return campeoes
 
def le_banco():
    dao = PilotoDAO()
    p = Piloto()
    lista = dao.pesquisa_todos(p)
    return lista
 
 
 
le_arquivo("/home/fernanda/Projects/nosql/formula1.txt")