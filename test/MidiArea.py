import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class MdiExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMdiArea Example")
        self.setGeometry(100, 100, 800, 600)

        # Crear un QMdiArea
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # Crear acciones para el menú
        new_action = QAction("Nuevo Documento", self)
        new_action.triggered.connect(self.create_new_document)

        cascade_action = QAction("Organizar en Cascada", self)
        cascade_action.triggered.connect(self.mdi_area.cascadeSubWindows)

        tile_action = QAction("Organizar en Mosaico", self)
        tile_action.triggered.connect(self.mdi_area.tileSubWindows)

        # Crear una barra de menús
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Archivo")
        file_menu.addAction(new_action)
        window_menu = menu_bar.addMenu("Ventana")
        window_menu.addAction(cascade_action)
        window_menu.addAction(tile_action)

    def create_new_document(self):
        # Crear una nueva sub-ventana
        sub_window = QMdiSubWindow()
        text_edit = QTextEdit()
        sub_window.setWidget(text_edit)
        sub_window.setWindowTitle("Nuevo Documento")
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MdiExample()
    window.show()

    sys.exit(app.exec())
