import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from PySide6.QtCore import QAbstractTableModel, Qt

class ExpenseTableModel(QAbstractTableModel):
    def __init__(self, expenses):
        super().__init__()
        self.expenses = expenses
        self.headers = ["Fecha", "Descripción", "Categoría", "Monto"]

    def rowCount(self, parent=None):
        # Incluimos una fila adicional para el total
        return len(self.expenses) + 1

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if index.row() < len(self.expenses):
                return self.expenses[index.row()][index.column()]
            elif index.row() == len(self.expenses):
                if index.column() == 0:
                    return "Total"
                elif index.column() == 3:
                    return str(self.calculate_total())
                else:
                    return ""

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headers[section]

    def calculate_total(self):
        total = sum(expense[3] for expense in self.expenses)
        return total

# Datos de ejemplo
expenses = [
    ["2024-06-01", "Supermercado", "Alimentación", 50.0],
    ["2024-06-02", "Gasolina", "Transporte", 40.0],
    ["2024-06-03", "Restaurante", "Ocio", 30.0],
]

class TableViewApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableView Total Example")
        self.setGeometry(100, 100, 600, 400)

        # Crear el widget central y su layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # QTableView para mostrar los gastos
        self.table_view = QTableView()
        layout.addWidget(self.table_view)

        # Modelo de datos
        self.model = ExpenseTableModel(expenses)
        self.table_view.setModel(self.model)

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TableViewApp()
    window.show()

    sys.exit(app.exec())
