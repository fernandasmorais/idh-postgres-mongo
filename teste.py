from pymongo import MongoClient
 
class MongoDBApp:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="puc", collection_name="usuário"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
 
    def consultar(self, filtro={}):
        documentos = self.collection.find(filtro)
        for doc in documentos:
            print(doc)
 
    def incluir(self, documento):
        resultado = self.collection.insert_one(documento)
        print(f"Documento inserido com _id: {resultado.inserted_id}")
 
    def alterar(self, filtro, novos_valores):
        atualizacao = {"$set": novos_valores}
        resultado = self.collection.update_many(filtro, atualizacao)
        print(f"{resultado.modified_count} documento(s) alterado(s).")
 
    def excluir(self, filtro):
        resultado = self.collection.delete_many(filtro)
        print(f"{resultado.deleted_count} documento(s) excluído(s).")
 
 
# ===========================
# Exemplo de uso do programa
# ===========================
 
if __name__ == "__main__":
    app = MongoDBApp()
 
    # Inserir um novo documento
    novo_doc = {"nome": "manteiga", "valor": 30.0}
    app.incluir(novo_doc)
 
    ''''  # Alterar documentos onde nome = "Maria"
    filtro = {"nome": "feijao"}
    novos_dados = {"valor": 25.0}
    app.alterar(filtro, novos_dados)
 
    # Excluir documentos onde nome = "Maria"
    filtro = {"nome": "manteiga"}
    app.excluir(filtro)'''
 
    # Consultar todos os documentos
    app.consultar()