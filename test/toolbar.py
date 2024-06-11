import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QVBoxLayout, QWidget, QMenuBar
from PySide6.QtGui import *

class MainWindowApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMainWindow Example")
        self.setGeometry(100, 100, 800, 600)

        # Crear barra de menús
        self.create_menu_bar()

        # Crear barra de herramientas
        self.create_tool_bar()

        # Crear el widget central y su layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

    def create_menu_bar(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("Archivo")
        edit_menu = menu_bar.addMenu("Editar")

        new_action = QAction("Nuevo", self)
        open_action = QAction("Abrir", self)
        save_action = QAction("Guardar", self)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

    def create_tool_bar(self):
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        new_action = QAction("Nuevo", self)
        open_action = QAction("Abrir", self)
        save_action = QAction("Guardar", self)

        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindowApp()
    window.show()

    sys.exit(app.exec())
