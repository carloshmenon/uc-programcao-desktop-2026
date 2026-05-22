
    #adm@gmail.com
    #123
import sys
from PySide6.QtWidgets import QApplication
from model.database import inicializar_banco
from controller.login_controller import LoginController # Garanta a ortografia correta da pasta

if __name__ == "__main__":
    # 1. Garante a criação segura do banco de dados e das tabelas limpas
    inicializar_banco()
    
    # 2. Inicializa a aplicação gráfica do PySide6
    app = QApplication(sys.argv)
    
    # 3. Abre a tela de login
    tela_login = LoginController()
    tela_login.show()
    
    sys.exit(app.exec())