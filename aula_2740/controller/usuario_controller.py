from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from model.usuario_model import UsuarioModel


class UsuarioController:

    def __init__(self):
        loader = QUiLoader()
        file = QFile("view/home.ui")
        file.open(QFile.ReadOnly)

        self.window = loader.load(file)
        file.close()

        self.model = UsuarioModel()

        self.window.btnAdicionar.clicked.connect(self.adicionar)
        self.window.btnExcluir.clicked.connect(self.deletar)

        self.carregar()

    def carregar(self):
        self.window.listaUsuarios.clear()

        for usuario in self.model.listar():
            texto = f"{usuario[0]} - {usuario[1]} ({usuario[2]})"
            self.window.listaUsuarios.addItem(texto)

    def adicionar(self):
        nome = self.window.inputNome.text()
        email = self.window.inputEmail.text()
        senha = self.window.inputSenha.text()

        self.model.adicionar(nome, email, senha)
        self.carregar()

    def deletar(self):
        item = self.window.listaUsuarios.currentItem()

        if item:
            id = int(item.text().split(" - ")[0])
            self.model.deletar(id)
            self.carregar()

    def show(self):
        self.window.show()