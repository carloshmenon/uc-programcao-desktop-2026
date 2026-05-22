from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView
from model.servico_model import ServicoModel  # Importa o modelo específico de serviços

class ServicosController:

    def __init__(self):
        loader = QUiLoader()
        file = QFile("view/servicos.ui")
        file.open(QFile.ReadOnly)
        self.window = loader.load(file)
        file.close()

        # Correção: Instanciando o modelo correto para Serviços
        self.model = ServicoModel()

        self.window.stackedWidget.setCurrentIndex(0)

        # Configura os botões contidos na própria janela independente de Serviços
        self.window.btnMenuServicos.clicked.connect(self.listar_servicos)
        self.window.btnNovoServico.clicked.connect(self.novo_servico)
        self.window.btnSalvarServico.clicked.connect(self.inserir_servico)
        self.window.tabelaServicos.cellDoubleClicked.connect(self.abrir_edicao)

    def listar_servicos(self):
        self.window.stackedWidget.setCurrentIndex(1)

        # Correção: Chamada limpa sem enviar 'self'
        dados = self.model.listar()

        self.window.tabelaServicos.setRowCount(len(dados))
        self.window.tabelaServicos.verticalHeader().setVisible(False)
        self.window.tabelaServicos.setSelectionBehavior(
            self.window.tabelaServicos.SelectionBehavior.SelectRows
        )
        self.window.tabelaServicos.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        for linha, servico in enumerate(dados):
            self.window.tabelaServicos.setItem(linha, 0, QTableWidgetItem(str(servico[0])))
            self.window.tabelaServicos.setItem(linha, 1, QTableWidgetItem(servico[1]))
            self.window.tabelaServicos.setItem(linha, 2, QTableWidgetItem(servico[2]))
            self.window.tabelaServicos.setItem(linha, 3, QTableWidgetItem(servico[3]))

    def nova_servico(self):
        self.window.stackedWidget.setCurrentIndex(2)

    def inserir_servico(self):
        servico = self.window.inputServico.text()
        valor = self.window.inputValor.text()
        descricao = self.window.inputDescricao.toPlainText()

        # Correção: Gravando na tabela correta
        self.model.inserir(servico, valor, descricao)

        # Limpa os formulários
        self.window.inputServico.clear()
        self.window.inputValor.clear()
        self.window.inputDescricao.clear()

        self.listar_servicos()

    def abrir_edicao(self, row):
        servico = self.window.tabelaServicos.item(row, 1).text()
        valor = self.window.tabelaServicos.item(row, 2).text()
        descricao = self.window.tabelaServicos.item(row, 3).text()

        self.window.stackedWidget.setCurrentIndex(2)

        self.window.inputServico.setText(servico)
        self.window.inputValor.setText(valor)
        self.window.inputDescricao.setPlainText(descricao)

    def show(self):
        self.window.show()