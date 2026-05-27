import sqlite3

class ClienteModel:
    def __init__(self):
       self.db_name = "oficina.db"
       
    def listar(self):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email, telefone FROM clientes")
        dados = cursor.fetchall()
        conexao.close()
        return dados

    def inserir(self, nome, email, telefone):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
            (nome, email, telefone)
        )
        conexao.commit()
        conexao.close()