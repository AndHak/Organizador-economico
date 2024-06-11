import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TableWidgetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget Example")
        self.setGeometry(100, 100, 800, 600)

        # Crear el widget central y su layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # QTableWidget para transacciones detalladas
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(10)
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["Fecha", "Descripción", "Categoría", "Monto", "Tipo"])
        layout.addWidget(self.table_widget)

        # Añadir algunos items de ejemplo al QTableWidget
        self.populate_table_widget()

        self.setCentralWidget(central_widget)

    def populate_table_widget(self):
        for row in range(10):
            self.table_widget.setItem(row, 0, QTableWidgetItem(f"2024-06-{row + 1:02d}"))
            self.table_widget.setItem(row, 1, QTableWidgetItem(f"Descripción {row + 1}"))
            self.table_widget.setItem(row, 2, QTableWidgetItem("Gastos"))
            self.table_widget.setItem(row, 3, QTableWidgetItem(f"{100 + row * 10}"))
            self.table_widget.setItem(row, 4, QTableWidgetItem("Gasto"))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TableWidgetApp()
    window.show()

    sys.exit(app.exec())
