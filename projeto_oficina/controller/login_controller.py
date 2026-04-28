from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
#from model.usuario_model import UsuarioModel
from controller.usuario_controller import UsuarioController

class LoginController:

    def __init__(self):
        loader = QUiLoader()
        file = QFile("view/login.ui")
        file.open(QFile.ReadOnly)

        self.window = loader.load(file)
        file.close()
        #self.model = UsuarioController()
        self.window.btnLoginEntrar.clicked.connect(self.login)

    def login(self):
        email = self.window.inputLoginEmail.text()
        senha = self.window.inputLoginSenha.text()

        usuario = True  #self.model.validar_login(email, senha)

        if usuario:
            self.abrir_home()
    
    def abrir_home(self):
        self.home = UsuarioController()
        self.home.show()
        self.window.close()       

    def show(self):
        self.window.show()