from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from client.chat_client import ChatClient
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        ui_file = QFile("ui/tela.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()
        self.client = ChatClient()
        self.client.start()
        self.ui.btnEnviar.clicked.connect(self.enviar_mensagem)
        self.client.on_message(self.mostrar_mensagem)

    def enviar_mensagem(self):
        msg = self.ui.lineMensagem.text()
        self.client.send(msg)
        self.ui.lineMensagem.clear()

    def mostrar_mensagem(self, msg):
        self.ui.textChat.append(msg)
