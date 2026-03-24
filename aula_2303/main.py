import sys
from PySide6.QtWidgets import QApplication
from client.main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.ui.show()

sys.exit(app.exec())