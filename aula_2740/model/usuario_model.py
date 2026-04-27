from database.conexao import conectar


class UsuarioModel:

    def validar_login(self, email, senha):
        conn = conectar()
        cursor = conn.cursor()

        sql = "SELECT * FROM usuarios WHERE email=%s AND senha=%s"
        cursor.execute(sql, (email, senha))

        usuario = cursor.fetchone()

        conn.close()
        return usuario

    def listar(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios")
        dados = cursor.fetchall()

        conn.close()
        return dados

    def adicionar(self, nome, email, senha):
        conn = conectar()
        cursor = conn.cursor()

        sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, email, senha))

        conn.commit()
        conn.close()

    def deletar(self, id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
        conn.commit()

        conn.close()