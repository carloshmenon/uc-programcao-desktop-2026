from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QTableWidgetItem
from model.usuario_model import UsuarioModel
from model.usuario import Usuario
from PySide6.QtWidgets import QHeaderView


        
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
        self.window.tabelaUsuarios.cellDoubleClicked.connect(self.abrir_edicao)


    def listar_usuarios(self):
        self.window.stackedWidget.setCurrentIndex(1)

        dados = self.model.listar(self)

        self.window.tabelaUsuarios.setRowCount(len(dados))
        #retira a coluna vertical de numeros
        self.window.tabelaUsuarios.verticalHeader().setVisible(False)

        #Permite a seleção da linha
        self.window.tabelaUsuarios.setSelectionBehavior(
            self.window.tabelaUsuarios.SelectionBehavior.SelectRows
        )

        #faz o auto ajuste das colunas
        self.window.tabelaUsuarios.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

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

    def abrir_edicao(self, row):

        id = int(self.window.tabelaUsuarios.item(row, 0).text())
        nome = self.window.tabelaUsuarios.item(row, 1).text()
        email = self.window.tabelaUsuarios.item(row, 2).text()
        senha = self.window.tabelaUsuarios.item(row, 3).text()

      
        self.window.stackedWidget.setCurrentIndex(2)
        
        self.window.inputCadUsuarioNome.setText(nome)
        self.window.inputCadUsuarioEmail.setText(email)
        self.window.inputCadUsuarioSenha.setText(senha)
    

    def show(self):
        self.window.show()

    
