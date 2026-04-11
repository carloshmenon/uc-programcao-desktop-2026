import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainWindow:
    def __init__(self):
        loader = QUiLoader()
        file = QFile("tela.ui")

        if not file.open(QFile.ReadOnly):
            print("Erro ao abrir UI")
            sys.exit(-1)

        self.window = loader.load(file)
        file.close()

        #Eventos dos menus
        self.window.menuItemServico.triggered.connect(self.telaServico)
        self.window.menuItemNovoUsuario.triggered.connect(self.telaNovoUsuario)
        self.window.menuItemNovoCliente.triggered.connect(self.telaNovoCliente)
    
    def telaServico(self):
        self.window.stackedWidget.setCurrentIndex(2)
    
    def telaNovoUsuario(self):
        self.window.stackedWidget.setCurrentIndex(1)
    
    def telaNovoCliente(self):
        self.window.stackedWidget.setCurrentIndex(0)
    
    def show(self):
        self.window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()

    sys.exit(app.exec())
    