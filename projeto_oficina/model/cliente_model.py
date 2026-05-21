# model/cliente_model.py
# Substitui 'sua_conexao' pelo nome do teu ficheiro/módulo de base de dados
from database.conexao import conexao

class ClienteModel:

    @staticmethod
    def inserir(nome, email, telefone):
        conexao = conexao.conectar()
        cursor = conexao.cursor()
        # GARANTE QUE É A TABELA CLIENTES
        sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, email, telefone))
        conexao.commit()
        cursor.close()
        conexao.close()

    @staticmethod
    def listar():
        conexao = conexao.conectar()
        cursor = conexao.cursor()
        # GARANTE QUE PROCURA NA TABELA CLIENTES
        sql = "SELECT id, nome, email, telefone FROM clientes"
        cursor.execute(sql)
        dados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return dados # Retorna apenas os registros da tabela clientes