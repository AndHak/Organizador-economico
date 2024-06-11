from economix_ui_ui import Ui_MainWindow
from creacion_tabla import PandasModel
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import pandas as pd
import sys


class MyOrganizerApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")

        self.icon_name_widget.setHidden(True)
        self.dashboard_1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard_2.clicked.connect(self.switch_to_dashboardPage)

        self.new_1_button.clicked.connect(self.switch_to_newPage)
        self.new_2_button.clicked.connect(self.switch_to_newPage)

        self.settings_1.clicked.connect(self.switch_to_settingsPage)
        self.settings_2.clicked.connect(self.switch_to_settingsPage)

        self.about_us_button.clicked.connect(self.switch_to_aboutusPage)
        self.support_button.clicked.connect(self.switch_to_supportPage)

        self.checkbox_suborganizador.hide()
        self.combobox_suborganizador.hide()

        self.checkbox_organizador.stateChanged.connect(self.mostar_creacion_de_sub_tabla)
        self.checkbox_suborganizador.stateChanged.connect(self.mostar_creacion_de_sub_tabla_sub)
        self.combobox_organizador.currentIndexChanged.connect(self.mostrar_hijos_por_organizador)

        self.agragar_nuevo_organizador_button.clicked.connect(self.evaluar_nuevo_organizador)
        self.edit_save_button.clicked.connect(self.edit_all)

        self.treeWidget_organizadores.itemSelectionChanged.connect(self.mostrar_tabla_seleccionada)

        self.dashboard_1.click()

        self.lineedit_nombretabla.setStyleSheet("""QLineEdit {
    background-color: rgb(103, 178, 98); /* Color de fondo */
    border-top-left-radius: 20px; /* Radio de borde superior izquierdo */
    border-top-right-radius: 20px; /* Radio de borde superior derecho */
    font-size: 20px; /* Tamaño de fuente */
    font-weight: bold; /* Peso de la fuente */
    padding: 8px 20px; /* Espaciado dentro del line edit */
    color: white; /* Color del texto */
    border: 1px solid gray; /* Borde del line edit */
}
""")

        # Estructura para almacenar las tablas creadas
        self.tablas = {}
        self.selected_color = "#67B262"
        self.setup_color_buttons()

        self.treeWidget_organizadores.itemChanged.connect(self.actualizar_nombre_organizador)


    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentWidget(self.Dashboard_page)

    def switch_to_newPage(self):
        self.stackedWidget.setCurrentWidget(self.nuevo_organizador_page)

    def switch_to_supportPage(self):
        self.stackedWidget.setCurrentWidget(self.suppot_page)

    def switch_to_aboutusPage(self):
        self.stackedWidget.setCurrentWidget(self.about_us_page)

    def switch_to_settingsPage(self):
        self.stackedWidget.setCurrentWidget(self.Settings_page)

    def mostar_creacion_de_sub_tabla(self):
        if self.checkbox_organizador.isChecked():
            self.checkbox_suborganizador.show()
            self.combobox_suborganizador.show()
            self.actualizar_combobox_organizadores()
            self.combobox_organizador.setEnabled(True)
        else:
            self.checkbox_suborganizador.hide()
            self.combobox_suborganizador.hide()
            self.combobox_organizador.setEnabled(False)
            self.combobox_organizador.clear()

    def mostar_creacion_de_sub_tabla_sub(self):
        if self.checkbox_suborganizador.isChecked():
            self.combobox_suborganizador.setEnabled(True)
            self.mostrar_hijos_por_organizador()
        else:
            self.combobox_suborganizador.setEnabled(False)
            self.combobox_suborganizador.clear()

    def actualizar_combobox_organizadores(self):
        self.combobox_organizador.clear()
        for i in range(self.treeWidget_organizadores.topLevelItemCount()):
            organizador = self.treeWidget_organizadores.topLevelItem(i)
            self.combobox_organizador.addItem(organizador.text(0))

    def mostrar_hijos_por_organizador(self):
        self.combobox_suborganizador.clear()
        organizador_seleccionado = self.combobox_organizador.currentText()

        for i in range(self.treeWidget_organizadores.topLevelItemCount()):
            organizador = self.treeWidget_organizadores.topLevelItem(i)

            if organizador.text(0) == organizador_seleccionado:
                if organizador.childCount() > 0:
                    if self.checkbox_suborganizador.isChecked():
                        for j in range(organizador.childCount()):
                            child = organizador.child(j)
                            self.combobox_suborganizador.addItem(child.text(0))

    def evaluar_nuevo_organizador(self):
        nombre = self.lineedit_nuevoorganizaor.text().strip()
        if not nombre:
            self.mostrar_error("El nombre del organizador es obligatorio")
            return

        organizador_abuelo = self.combobox_organizador.currentText().strip()
        organizador_padre = self.combobox_suborganizador.currentText().strip()

        nuevo_organizador = QTreeWidgetItem([nombre])
        self.tablas[nombre] = {
            'dataframe': self.crear_nueva_tabla(),
            'color': self.selected_color if self.selected_color else "#67B262"
        }

        if not organizador_abuelo and not organizador_padre:
            self.treeWidget_organizadores.addTopLevelItem(nuevo_organizador)
        elif organizador_abuelo and not organizador_padre:
            item_abuelo = None
            for i in range(self.treeWidget_organizadores.topLevelItemCount()):
                item = self.treeWidget_organizadores.topLevelItem(i)
                if item.text(0) == organizador_abuelo:
                    item_abuelo = item
                    break
            if item_abuelo is None:
                item_abuelo = QTreeWidgetItem([organizador_abuelo])
                self.treeWidget_organizadores.addTopLevelItem(item_abuelo)
            item_abuelo.addChild(nuevo_organizador)
        elif organizador_abuelo and organizador_padre:
            item_abuelo = None
            for i in range(self.treeWidget_organizadores.topLevelItemCount()):
                item = self.treeWidget_organizadores.topLevelItem(i)
                if item.text(0) == organizador_abuelo:
                    item_abuelo = item
                    break
            if item_abuelo:
                item_padre = None
                for i in range(item_abuelo.childCount()):
                    item = item_abuelo.child(i)
                    if item.text(0) == organizador_padre:
                        item_padre = item
                        break
                if item_padre is None:
                    item_padre = QTreeWidgetItem([organizador_padre])
                    item_abuelo.addChild(item_padre)
                item_padre.addChild(nuevo_organizador)
            else:
                self.mostrar_error("El organizador abuelo seleccionado no se encontró.")


    def crear_nueva_tabla(self):
        # Crea un DataFrame de pandas con las columnas especificadas
        return pd.DataFrame(columns=['Descripción', 'Fecha', 'Hora', 'Valor'])

    def mostrar_tabla_seleccionada(self):
        selected_item = self.treeWidget_organizadores.currentItem()
        if selected_item:
            nombre_tabla = selected_item.text(0)
            if nombre_tabla in self.tablas:
                # Verifica que lineedit_nombretabla esté definido
                if hasattr(self, 'lineedit_nombretabla'):
                    self.lineedit_nombretabla.setText(nombre_tabla)
                model = PandasModel(self.tablas[nombre_tabla])
                self.tableView.setModel(model)

    def mostrar_tabla_seleccionada(self):
        selected_item = self.treeWidget_organizadores.currentItem()
        if selected_item:
            nombre_tabla = selected_item.text(0)
            if nombre_tabla in self.tablas:
                # Verifica que lineedit_nombretabla esté definido
                if hasattr(self, 'lineedit_nombretabla'):
                    self.lineedit_nombretabla.setText(nombre_tabla)
                    
                    # Obtener el color almacenado
                    color = self.tablas[nombre_tabla]['color']
                    
                    # Actualizar el estilo del lineedit_nombretabla
                    self.lineedit_nombretabla.setStyleSheet(f"""
                        QLineEdit {{
                            background-color: {color}; /* Color de fondo */
                            border-top-left-radius: 20px; /* Radio de borde superior izquierdo */
                            border-top-right-radius: 20px; /* Radio de borde superior derecho */
                            font-size: 20px; /* Tamaño de fuente */
                            font-weight: bold; /* Peso de la fuente */
                            padding: 8px 20px; /* Espaciado dentro del line edit */
                            color: white; /* Color del texto */
                            border: 1px solid gray; /* Borde del line edit */
                        }}
                    """)
                model = PandasModel(self.tablas[nombre_tabla]['dataframe'])
                self.tableView.setModel(model)

    def edit_all(self):
        if self.edit_save_button.text() == "Editar":
            self.edit_save_button.setText("Guardar")
            self.treeWidget_organizadores.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)
        else:
            self.edit_save_button.setText("Editar")
            self.treeWidget_organizadores.setEditTriggers(QAbstractItemView.NoEditTriggers)

            # Guardar los cambios en los nombres de los organizadores
            for i in range(self.treeWidget_organizadores.topLevelItemCount()):
                item = self.treeWidget_organizadores.topLevelItem(i)
                self.actualizar_nombre_organizador(item, 0)
                for j in range(item.childCount()):
                    child = item.child(j)
                    self.actualizar_nombre_organizador(child, 0)

    def actualizar_nombre_organizador(self, item, column):
        nuevo_nombre = item.text(column)
        nombre_antiguo = item.data(column, Qt.UserRole)
        
        if nombre_antiguo and nuevo_nombre:
            # Actualizar la entrada en self.tablas
            self.tablas[nuevo_nombre] = self.tablas.pop(nombre_antiguo)
            
            # También actualizar el UserRole con el nuevo nombre
            item.setData(column, Qt.UserRole, nuevo_nombre)
        elif not nuevo_nombre:
            self.mostrar_error("El nombre del organizador no puede estar vacío.")
            item.setText(column, nombre_antiguo)



    def find_tree_item(self, parent, text):
        for i in range(parent.childCount()):
            item = parent.child(i)
            if item.text(0) == text:
                return item
        return None



    def setup_color_buttons(self):
        self.color_buttons = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5, self.pushButton_6]
        for button in self.color_buttons:
            button.clicked.connect(self.color_button_clicked)

    def color_button_clicked(self):
        for button in self.color_buttons:
            if button.isChecked():
                self.selected_color = button.palette().button().color().name()
                break


    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyOrganizerApp()

    window.show()
    app.exec()
