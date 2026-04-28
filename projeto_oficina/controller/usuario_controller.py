from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
#from model.usuario_model import UsuarioModel
        
class UsuarioController:

    def __init__(self):
        loader = QUiLoader()
        file = QFile("view/home.ui")
        file.open(QFile.ReadOnly)

        self.window = loader.load(file)
        file.close()

        self.window.stackedWidget.setCurrentIndex(0)

        #self.model = UsuarioModel()

    def show(self):
        self.window.show()

        

