from PySide6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QDialogButtonBox, QLabel

class LocationDialog(QDialog):
    def __init__(self, parent=None, categories=None):
        super().__init__(parent)
        
        self.setWindowTitle("Seleccionar Ubicación")
        
        self.layout = QVBoxLayout(self)
        
        self.label_category = QLabel("Seleccione Categoría:")
        self.layout.addWidget(self.label_category)
        
        self.category_combobox = QComboBox(self)
        self.category_combobox.addItem("Ninguno")
        if categories:
            self.category_combobox.addItems(categories)
        self.category_combobox.currentTextChanged.connect(self.update_subcategories)
        self.layout.addWidget(self.category_combobox)
        
        self.label_subcategory = QLabel("Seleccione Subcategoría:")
        self.layout.addWidget(self.label_subcategory)
        
        self.subcategory_combobox = QComboBox(self)
        self.subcategory_combobox.addItem("Ninguno")
        self.layout.addWidget(self.subcategory_combobox)
        
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)
        
    def update_subcategories(self, category):
        self.subcategory_combobox.clear()
        self.subcategory_combobox.addItem("Ninguno")
        if category != "Ninguno":
            subcategories = self.load_subcategories(category)
            self.subcategory_combobox.addItems(subcategories)
        
    def load_subcategories(self, category):
        subcategories = []
        for i in range(self.parent().treeWidget_organizadores.topLevelItemCount()):
            item = self.parent().treeWidget_organizadores.topLevelItem(i)
            if item.text(0) == category:
                subcategories = [item.child(j).text(0) for j in range(item.childCount())]
                break
        return subcategories
        
    def get_inputs(self):
        return (self.category_combobox.currentText(), 
                self.subcategory_combobox.currentText())
