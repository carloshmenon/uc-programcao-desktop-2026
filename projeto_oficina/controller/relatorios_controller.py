from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QHeaderView

from model.usuario_model import UsuarioModel


class RelatoriosController:

    def __init__(self):

        loader = QUiLoader()

        file = QFile("view/relatorios.ui")
        file.open(QFile.ReadOnly)

        self.window = loader.load(file)
        file.close()

        self.model = UsuarioModel

        self.window.stackedWidget.setCurrentIndex(0)

        # BOTÕES
        self.window.btnRelatorioClientes.clicked.connect(
            self.relatorio_clientes
        )

        self.window.btnRelatorioBicicletas.clicked.connect(
            self.relatorio_bicicletas
        )

        self.window.btnRelatorioServicos.clicked.connect(
            self.relatorio_servicos
        )

        self.window.btnGerarPdf.clicked.connect(
            self.gerar_pdf
        )

    # CLIENTES
    def relatorio_clientes(self):

        self.window.stackedWidget.setCurrentIndex(1)

        dados = self.model.listar(self)

        self.preencher_tabela(dados)

    # BICICLETAS
    def relatorio_bicicletas(self):

        self.window.stackedWidget.setCurrentIndex(1)

        dados = self.model.listar(self)

        self.preencher_tabela(dados)

    # SERVIÇOS
    def relatorio_servicos(self):

        self.window.stackedWidget.setCurrentIndex(1)

        dados = self.model.listar(self)

        self.preencher_tabela(dados)

    # PREENCHER TABELA
    def preencher_tabela(self, dados):

        self.window.tabelaRelatorios.setRowCount(len(dados))

        self.window.tabelaRelatorios.verticalHeader().setVisible(False)

        self.window.tabelaRelatorios.setSelectionBehavior(
            self.window.tabelaRelatorios.SelectionBehavior.SelectRows
        )

        self.window.tabelaRelatorios.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        for linha, item in enumerate(dados):

            self.window.tabelaRelatorios.setItem(
                linha,
                0,
                QTableWidgetItem(str(item[0]))
            )

            self.window.tabelaRelatorios.setItem(
                linha,
                1,
                QTableWidgetItem(item[1])
            )

            self.window.tabelaRelatorios.setItem(
                linha,
                2,
                QTableWidgetItem(item[2])
            )

            self.window.tabelaRelatorios.setItem(
                linha,
                3,
                QTableWidgetItem(item[3])
            )

    # PDF
    def gerar_pdf(self):

        print("Gerando PDF...")

    def show(self):
        self.window.show()