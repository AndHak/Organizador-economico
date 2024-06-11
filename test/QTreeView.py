import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QFileSystemModel, QVBoxLayout, QWidget

class TreeViewApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTreeView Example")
        self.setGeometry(100, 100, 800, 600)

        # Crear el widget central y su layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # QTreeView para mostrar el sistema de archivos
        self.tree_view = QTreeView()
        layout.addWidget(self.tree_view)

        # Modelo de sistema de archivos
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(''))

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TreeViewApp()
    window.show()

    sys.exit(app.exec())
