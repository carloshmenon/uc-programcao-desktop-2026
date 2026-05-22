import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect("database/oficina.db")
    cursor = conexao.cursor()
    
    # Tabela de Usuários (Apenas para o login do sistema e funcionários)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)
    
    # Tabela de Clientes (Separada dos logins)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)
    
    # Tabela de Serviços
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            servico TEXT NOT NULL,
            valor TEXT NOT NULL,
            descricao TEXT
        )
    """)
    
    # Inserir um usuário padrão caso a tabela esteja vazia para você conseguir logar
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES ('Administrador', 'admin@mail.com', '1234')")
    
    conexao.commit()
    conexao.close()