import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from PySide6.QtCore import QAbstractTableModel, Qt

class SimpleTableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.data = [
            ["2024-06-01", "Descripción 1", "Gastos", "100", "Gasto"],
            ["2024-06-02", "Descripción 2", "Gastos", "110", "Gasto"],
            # Añadir más filas si es necesario
        ]
        self.headers = ["Fecha", "Descripción", "Categoría", "Monto", "Tipo"]

    def rowCount(self, parent=None):
        return len(self.data)

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.data[index.row()][index.column()]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headers[section]
            else:
                return section + 1

class TableViewApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableView Example")
        self.setGeometry(100, 100, 800, 600)

        # Crear el widget central y su layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # QTableView para mostrar datos de ejemplo
        self.table_view = QTableView()
        layout.addWidget(self.table_view)

        # Modelo de datos
        self.model = SimpleTableModel()
        self.table_view.setModel(self.model)

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TableViewApp()
    window.show()

    sys.exit(app.exec())
