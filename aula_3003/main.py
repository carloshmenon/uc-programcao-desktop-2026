import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MainWindow:
    def __init__(self):
        loader = QUiLoader()
        file = QFile("tela.ui")

        if not file.open(QFile.ReadOnly):
            print("Erro ao abrir tela.ui")
            sys.exit(-1)

        self.window  = loader.load(file)
        file.close()
        self.window.setCurrentIndex(0)
        self.window.btnEntrar.clicked.connect(self.entrar)
        self.window.btnHomeVoltar.clicked.connect(self.voltar)        
        self.window.btnSobreVoltar.clicked.connect(self.voltar)
        self.window.btnHomeSobre.clicked.connect(self.sobre)

    def entrar(self):
        login = self.window.textLogin.text()

        if login.strip() == "":
            return
        self.window.labelHome.setText(f"Bem Vindo, {login}!!")
        self.window.setCurrentIndex(1)
     
    def sobre(self):
        self.window.setCurrentIndex(2)
    
    def voltar(self):
        self.window.setCurrentIndex(0)   

    def show(self):
        self.window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()

    sys.exit(app.exec())
