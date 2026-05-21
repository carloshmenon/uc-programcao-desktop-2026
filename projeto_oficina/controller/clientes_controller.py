from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView
from model.cliente_model import ClienteModel

class ClientesController:

    def __init__(self, main_window=None):
        loader = QUiLoader()

        file = QFile("view/clientes.ui")
        file.open(QFile.ReadOnly)
        self.window = loader.load(file)
        file.close()

        # Guarda a referência da Home para poder alternar as páginas no stackedWidget global
        self.main_window = main_window
        
        # Reutilizando UsuarioModel
        self.model = ClienteModel

        # --- BOTÕES ---
        # Como o botão Salvar está neste arquivo .ui, conectamos ele aqui:
        self.window.btnSalvarCliente.clicked.connect(self.inserir_cliente)

        # NOTA: Os botões de listar, trocar para aba de novo cliente e a tabela 
        # devem ser configurados no HomeController, pois pertencem à tela principal.

    # LISTAR (Atualiza a tabela que fica na main_window)
    def listar_clientes(self):
        if not self.main_window:
            return

        # Muda o index do stackedWidget da tela principal para a listagem
        self.main_window.stackedWidget.setCurrentIndex(1)

        dados = self.model.listar(self)
        
        # A tabela fica na janela principal (Home)
        tabela = self.main_window.tabelaClientes
        tabela.setRowCount(len(dados))

        # Remove números laterais
        tabela.verticalHeader().setVisible(False)

        # Selecionar linha inteira
        tabela.setSelectionBehavior(tabela.SelectionBehavior.SelectRows)

        # Ajustar colunas
        tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for linha, cliente in enumerate(dados):
            tabela.setItem(linha, 0, QTableWidgetItem(str(cliente[0])))
            tabela.setItem(linha, 1, QTableWidgetItem(cliente[1]))
            tabela.setItem(linha, 2, QTableWidgetItem(cliente[2]))
            tabela.setItem(linha, 3, QTableWidgetItem(cliente[3]))

    # INSERIR
    def inserir_cliente(self):
        # Nomes corrigidos de acordo com o seu arquivo XML!
        nome = self.window.inputNomeCliente.text()
        email = self.window.inputEmailCliente.text()
        telefone = self.window.inputTelefoneCliente.text()

        # Reutilizando o método inserir do seu model
        self.model.inserir(self, nome, email, telefone)
        
        # Limpa os campos após salvar
        self.window.inputNomeCliente.clear()
        self.window.inputEmailCliente.clear()
        self.window.inputTelefoneCliente.clear()

        # Recarrega a tabela
        self.listar_clientes()

    # EDITAR / PREENCHER FORMULÁRIO
    def abrir_edicao(self, row):
        if not self.main_window:
            return

        tabela = self.main_window.tabelaClientes
        
        id_cliente = int(tabela.item(row, 0).text())
        nome = tabela.item(row, 1).text()
        email = tabela.item(row, 2).text()
        telefone = tabela.item(row, 3).text()

        # Muda para o index do formulário de cadastro no seu stackedWidget global
        self.main_window.stackedWidget.setCurrentIndex(2)

        # Preenche os inputs do formulário com os dados da linha clicada
        self.window.inputNomeCliente.setText(nome)
        self.window.inputEmailCliente.setText(email)
        self.window.inputTelefoneCliente.setText(telefone)

    def show(self):
        self.window.show()