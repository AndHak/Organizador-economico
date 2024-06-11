import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget

class TreeWidgetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTreeWidget Example")
        self.setGeometry(100, 100, 600, 400)

        # Crear el widget central y su layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # QTreeWidget para categorías de gastos
        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(2)
        self.tree_widget.setHeaderLabels(["Categoría", "Descripción"])
        layout.addWidget(self.tree_widget)

        # Añadir algunos items de ejemplo al QTreeWidget
        self.populate_tree_widget()

        self.setCentralWidget(central_widget)

    def populate_tree_widget(self):
        # Crear elementos raíz
        alimentacion = QTreeWidgetItem(self.tree_widget)
        alimentacion.setText(0, "Alimentación")

        transporte = QTreeWidgetItem(self.tree_widget)
        transporte.setText(0, "Transporte")

        # Crear subelementos
        supermercado = QTreeWidgetItem(alimentacion)
        supermercado.setText(0, "Supermercado")
        supermercado.setText(1, "Compra mensual de alimentos")

        combustible = QTreeWidgetItem(transporte)
        combustible.setText(0, "Combustible")
        combustible.setText(1, "Gastos en gasolina")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TreeWidgetApp()
    window.show()

    sys.exit(app.exec())
