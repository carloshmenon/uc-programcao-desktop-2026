from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView
from model.cliente_model import ClienteModel  # Importa o modelo correto

class ClientesController:

    def __init__(self, main_window=None):
        loader = QUiLoader()
        file = QFile("view/clientes.ui")
        file.open(QFile.ReadOnly)
        self.window = loader.load(file)
        file.close()

        self.main_window = main_window
        
        # Correção: Instanciando o modelo com parênteses ()
        self.model = ClienteModel()

        # Botão Salvar da janela/widget de cadastro de clientes
        self.window.btnSalvarCliente.clicked.connect(self.inserir_cliente)

    def listar_clientes(self):
        if not self.main_window:
            return

        self.main_window.stackedWidget.setCurrentIndex(1)

        # Correção: Removido o 'self' de dentro dos argumentos do método
        dados = self.model.listar()
        
        tabela = self.main_window.tabelaClientes
        tabela.setRowCount(len(dados))
        tabela.verticalHeader().setVisible(False)
        tabela.setSelectionBehavior(tabela.SelectionBehavior.SelectRows)
        tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for linha, cliente in enumerate(dados):
            tabela.setItem(linha, 0, QTableWidgetItem(str(cliente[0])))
            tabela.setItem(linha, 1, QTableWidgetItem(cliente[1]))
            tabela.setItem(linha, 2, QTableWidgetItem(cliente[2]))
            tabela.setItem(linha, 3, QTableWidgetItem(cliente[3]))

    def inserir_cliente(self):
        nome = self.window.inputNomeCliente.text()
        email = self.window.inputEmailCliente.text()
        telefone = self.window.inputTelefoneCliente.text()

        # Correção: Removido o 'self' de dentro dos argumentos
        self.model.inserir(nome, email, telefone)
        
        self.window.inputNomeCliente.clear()
        self.window.inputEmailCliente.clear()
        self.window.inputTelefoneCliente.clear()

        self.listar_clientes()

    def abrir_edicao(self, row):
        if not self.main_window:
            return

        tabela = self.main_window.tabelaClientes
        nome = tabela.item(row, 1).text()
        email = tabela.item(row, 2).text()
        telefone = tabela.item(row, 3).text()

        self.main_window.stackedWidget.setCurrentIndex(2)

        self.window.inputNomeCliente.setText(nome)
        self.window.inputEmailCliente.setText(email)
        self.window.inputTelefoneCliente.setText(telefone)

    def show(self):
        self.window.show()