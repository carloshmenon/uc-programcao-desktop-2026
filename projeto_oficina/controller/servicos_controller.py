from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QHeaderView

from model.usuario_model import UsuarioModel


class ServicosController:

    def __init__(self):

        loader = QUiLoader()

        file = QFile("view/servicos.ui")
        file.open(QFile.ReadOnly)

        self.window = loader.load(file)
        file.close()

        # reutilizando UsuarioModel
        self.model = UsuarioModel

        # página inicial
        self.window.stackedWidget.setCurrentIndex(0)

        # BOTÕES
        self.window.btnMenuServicos.clicked.connect(
            self.listar_servicos
        )

        self.window.btnNovoServico.clicked.connect(
            self.novo_servico
        )

        self.window.btnSalvarServico.clicked.connect(
            self.inserir_servico
        )

        # TABELA
        self.window.tabelaServicos.cellDoubleClicked.connect(
            self.abrir_edicao
        )

    # LISTAR
    def listar_servicos(self):

        self.window.stackedWidget.setCurrentIndex(1)

        dados = self.model.listar(self)

        self.window.tabelaServicos.setRowCount(len(dados))

        # remove números laterais
        self.window.tabelaServicos.verticalHeader().setVisible(False)

        # selecionar linha inteira
        self.window.tabelaServicos.setSelectionBehavior(
            self.window.tabelaServicos.SelectionBehavior.SelectRows
        )

        # ajustar colunas
        self.window.tabelaServicos.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        for linha, servico in enumerate(dados):

            self.window.tabelaServicos.setItem(
                linha,
                0,
                QTableWidgetItem(str(servico[0]))
            )

            self.window.tabelaServicos.setItem(
                linha,
                1,
                QTableWidgetItem(servico[1])
            )

            self.window.tabelaServicos.setItem(
                linha,
                2,
                QTableWidgetItem(servico[2])
            )

            self.window.tabelaServicos.setItem(
                linha,
                3,
                QTableWidgetItem(servico[3])
            )

    # NOVO SERVIÇO
    def novo_servico(self):

        self.window.stackedWidget.setCurrentIndex(2)

    # INSERIR
    def inserir_servico(self):

        servico = self.window.inputServico.text()
        valor = self.window.inputValor.text()
        descricao = self.window.inputDescricao.toPlainText()

        # reutilizando UsuarioModel
        self.model.inserir(
            self,
            servico,
            valor,
            descricao
        )

        self.listar_servicos()

    # EDITAR
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