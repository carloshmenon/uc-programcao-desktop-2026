from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QHeaderView

from model.usuario_model import UsuarioModel


class ClientesController:

    def __init__(self):

        loader = QUiLoader()

        file = QFile("view/clientes.ui")
        file.open(QFile.ReadOnly)

        self.window = loader.load(file)
        file.close()

        # reutilizando UsuarioModel
        self.model = UsuarioModel

        self.window.stackedWidget.setCurrentIndex(0)

        # BOTÕES
        self.window.btnMenuClientes.clicked.connect(
            self.listar_clientes
        )

        self.window.btnNovoCliente.clicked.connect(
            self.novo_cliente
        )

        self.window.btnSalvarCliente.clicked.connect(
            self.inserir_cliente
        )

        # TABELA
        self.window.tabelaClientes.cellDoubleClicked.connect(
            self.abrir_edicao
        )

    # LISTAR
    def listar_clientes(self):

        self.window.stackedWidget.setCurrentIndex(1)

        dados = self.model.listar(self)

        self.window.tabelaClientes.setRowCount(len(dados))

        # remove números laterais
        self.window.tabelaClientes.verticalHeader().setVisible(False)

        # selecionar linha inteira
        self.window.tabelaClientes.setSelectionBehavior(
            self.window.tabelaClientes.SelectionBehavior.SelectRows
        )

        # ajustar colunas
        self.window.tabelaClientes.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        for linha, cliente in enumerate(dados):

            self.window.tabelaClientes.setItem(
                linha,
                0,
                QTableWidgetItem(str(cliente[0]))
            )

            self.window.tabelaClientes.setItem(
                linha,
                1,
                QTableWidgetItem(cliente[1])
            )

            self.window.tabelaClientes.setItem(
                linha,
                2,
                QTableWidgetItem(cliente[2])
            )

            self.window.tabelaClientes.setItem(
                linha,
                3,
                QTableWidgetItem(cliente[3])
            )

    # NOVO
    def novo_cliente(self):

        self.window.stackedWidget.setCurrentIndex(2)

    # INSERIR
    def inserir_cliente(self):

        nome = self.window.inputNome.text()
        email = self.window.inputEmail.text()
        senha = self.window.inputTelefone.text()

        # reutilizando método inserir
        self.model.inserir(
            self,
            nome,
            email,
            senha
        )

        self.listar_clientes()

    # EDITAR
    def abrir_edicao(self, row):

        id_cliente = int(
            self.window.tabelaClientes.item(row, 0).text()
        )

        nome = self.window.tabelaClientes.item(row, 1).text()

        email = self.window.tabelaClientes.item(row, 2).text()

        telefone = self.window.tabelaClientes.item(row, 3).text()

        self.window.stackedWidget.setCurrentIndex(2)

        self.window.inputNome.setText(nome)
        self.window.inputEmail.setText(email)
        self.window.inputTelefone.setText(telefone)

    def show(self):
        self.window.show()