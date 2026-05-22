import sqlite3

class ServicoModel:
    def __init__(self):
       self.db_name = "database/oficina.db"

    def listar(self):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute("SELECT id, servico, valor, descricao FROM servicos")
        dados = cursor.fetchall()
        conexao.close()
        return dados

    def inserir(self, servico, valor, descricao):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO servicos (servico, valor, descricao) VALUES (?, ?, ?)",
            (servico, valor, descricao)
        )
        conexao.commit()
        conexao.close()