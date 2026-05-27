from database.conexao import conectar

class BicicletasModel:


    def validar_bicicleta(self, marca, cor, telefone):
        conn = conectar()       
        cursor = conn.cursor()

        sql = "SELECT * FROM bicicletas WHERE marca=%s AND cor=%s AND telefone=%s"
        cursor.execute(sql, (marca, cor, telefone))
        
        usuario = cursor.fetchone()

        conn.close
        return usuario

    def listar(self):
        conn = conectar()       
        cursor = conn.cursor()

        sql = "SELECT * FROM bicicletas"
        cursor.execute(sql)
        dados = cursor.fetchall()

        conn.close
        return dados
    
    def inserir(self, marca, cor, telefone):  
        conn = conectar()       
        cursor = conn.cursor()

        sql = "INSERT INTO bicicletas(marca, cor, telefone) VALUES(%s, %s, %s)"
        cursor.execute(sql, (marca, cor, telefone))
        
        conn.commit()
        conn.close

    def deletar(self, id):
        conn = conectar()       
        cursor = conn.cursor()

        sql = "DELETE FROM bicicletas WHERE id=%s"
        cursor.execute(sql, (id))
        
        conn.commit()
        conn.close

    

        
    

    
