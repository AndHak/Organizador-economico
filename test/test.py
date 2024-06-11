import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class EconomicOrganizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Economic Organizer")
        self.setGeometry(100, 100, 800, 600)

        # Crear el menú
        self.create_menu()

        # Crear la barra de herramientas
        self.create_toolbar()

        # Crear el área central
        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

        # Agregar el árbol de categorías
        self.create_tree_widget()

        # Agregar una tabla
        self.create_table_widget()

    def create_menu(self):
        menu_bar = QMenuBar(self)
        file_menu = menu_bar.addMenu("Archivo")

        new_action = QAction("Nuevo", self)
        save_action = QAction("Guardar", self)
        load_action = QAction("Cargar", self)
        exit_action = QAction("Salir", self)

        file_menu.addAction(new_action)
        file_menu.addAction(save_action)
        file_menu.addAction(load_action)
        file_menu.addAction(exit_action)

        exit_action.triggered.connect(self.close)

        self.setMenuBar(menu_bar)

    def create_toolbar(self):
        toolbar = QToolBar("Toolbar", self)
        self.addToolBar(toolbar)

        new_action = QAction("Nuevo", self)
        save_action = QAction("Guardar", self)
        load_action = QAction("Cargar", self)

        toolbar.addAction(new_action)
        toolbar.addAction(save_action)
        toolbar.addAction(load_action)

    def create_tree_widget(self):
        tree_widget = QTreeWidget()
        tree_widget.setHeaderLabel("Categorías")
        categories = ["Ingresos", "Gastos", "Ahorros", "Inversiones"]
        for category in categories:
            item = QTreeWidgetItem([category])
            tree_widget.addTopLevelItem(item)

        dock_widget = QDockWidget("Categorías", self)
        dock_widget.setWidget(tree_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

    def create_table_widget(self):
        table_widget = QTableWidget(10, 5)  # 10 filas, 5 columnas
        table_widget.setHorizontalHeaderLabels(["Fecha", "Descripción", "Categoría", "Monto", "Tipo"])

        # Ejemplo de datos
        for row in range(10):
            table_widget.setItem(row, 0, QTableWidgetItem(f"2024-06-{row+1:02d}"))
            table_widget.setItem(row, 1, QTableWidgetItem(f"Descripción {row+1}"))
            table_widget.setItem(row, 2, QTableWidgetItem("Gastos"))
            table_widget.setItem(row, 3, QTableWidgetItem(f"{100 + row*10}"))
            table_widget.setItem(row, 4, QTableWidgetItem("Gasto"))

        dock_widget = QDockWidget("Transacciones", self)
        dock_widget.setWidget(table_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, dock_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EconomicOrganizer()
    window.show()
    sys.exit(app.exec())
