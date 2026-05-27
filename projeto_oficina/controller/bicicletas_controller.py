from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QHeaderView

from model.usuario_model import BicicletasModel


class BicicletasController:

    def __init__(self):

        loader = QUiLoader()

        file = QFile("view/bicicletas.ui")
        file.open(QFile.ReadOnly)

        self.window = loader.load(file)
        file.close()

        # reutilizando UsuarioModel
        self.model = BicicletasModel ()

        # página inicial
        self.window.stackedWidget.setCurrentIndex(0)

        # BOTÕES
        self.window.btnMenuBicicletas.clicked.connect(
            self.listar_bicicletas
        )

        self.window.btnNovaBicicleta.clicked.connect(
            self.nova_bicicleta
        )

        self.window.btnSalvarBicicleta.clicked.connect(
            self.inserir_bicicleta
        )

        # TABELA
        self.window.tabelaBicicletas.cellDoubleClicked.connect(
            self.abrir_edicao
        )

    # LISTAR
    def listar_bicicletas(self):

        self.window.stackedWidget.setCurrentIndex(1)

        dados = self.model.listar()

        self.window.tabelaBicicletas.setRowCount(len(dados))

        # remove números laterais
        self.window.tabelaBicicletas.verticalHeader().setVisible(False)

        # selecionar linha inteira
        self.window.tabelaBicicletas.setSelectionBehavior(
            self.window.tabelaBicicletas.SelectionBehavior.SelectRows
        )

        # ajustar colunas
        self.window.tabelaBicicletas.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        for linha, bicicleta in enumerate(dados):

            self.window.tabelaBicicletas.setItem(
                linha,
                0,
                QTableWidgetItem(str(bicicleta[0]))
            )

            self.window.tabelaBicicletas.setItem(
                linha,
                1,
                QTableWidgetItem(bicicleta[1])
            )

            self.window.tabelaBicicletas.setItem(
                linha,
                2,
                QTableWidgetItem(bicicleta[2])
            )

            self.window.tabelaBicicletas.setItem(
                linha,
                3,
                QTableWidgetItem(bicicleta[3])
            )

    # NOVA BICICLETA
    def nova_bicicleta(self):

        self.window.stackedWidget.setCurrentIndex(2)

    # INSERIR
    def inserir_bicicleta(self):

        marca = self.window.inputMarca.text()
        modelo = self.window.inputModelo.text()
        cor = self.window.inputCor.text()

        # reutilizando UsuarioModel
        self.model.inserir(
            
            marca,
            modelo,
            cor
        )

        self.listar_bicicletas()

    # EDITAR
    def abrir_edicao(self, row):

        marca = self.window.tabelaBicicletas.item(row, 1).text()

        modelo = self.window.tabelaBicicletas.item(row, 2).text()

        cor = self.window.tabelaBicicletas.item(row, 3).text()

        self.window.stackedWidget.setCurrentIndex(2)

        self.window.inputMarca.setText(marca)
        self.window.inputModelo.setText(modelo)
        self.window.inputCor.setText(cor)

    def show(self):
        self.window.show()