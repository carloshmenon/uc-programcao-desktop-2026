from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QTableWidgetItem
from model.usuario_model import UsuarioModel


        
class HomeController:

    def __init__(self):
        loader = QUiLoader()
        file = QFile("view/home.ui")
        file.open(QFile.ReadOnly)

        self.window = loader.load(file)
        file.close()

        self.model = UsuarioModel
        self.window.stackedWidget.setCurrentIndex(0)
        self.window.btnMenuUsuarios.clicked.connect(self.listar_usuarios)
        self.window.btnUsuariosNovo.clicked.connect(self.novo_usuario)
        self.window.btnCadUsuarioCadastrar.clicked.connect(self.inserir_usuario)


    def listar_usuarios(self):
        self.window.stackedWidget.setCurrentIndex(1)

        dados = self.model.listar(self)

        self.window.tabelaUsuarios.setRowCount(len(dados))

        for linha, usuario in enumerate(dados):
            self.window.tabelaUsuarios.setItem(linha, 0, QTableWidgetItem(str(usuario[0])))
            self.window.tabelaUsuarios.setItem(linha, 1, QTableWidgetItem(usuario[1]))
            self.window.tabelaUsuarios.setItem(linha, 2, QTableWidgetItem(usuario[2]))
            self.window.tabelaUsuarios.setItem(linha, 3, QTableWidgetItem(usuario[3]))
    
    def novo_usuario(self):
        self.window.stackedWidget.setCurrentIndex(2)

    def inserir_usuario(self):
        nome = self.window.inputCadUsuarioNome.text()
        email = self.window.inputCadUsuarioEmail.text()
        senha = self.window.inputCadUsuarioSenha.text()
        confirmar_senha =  self.window.inputCadUsuarioConfirmarSenha.text()

        if senha == confirmar_senha:
            self.model.inserir(self, nome, email, senha)
            self.listar_usuarios()
        else:
            print("As senhas não são iguais")

    def show(self):
        self.window.show()

    
