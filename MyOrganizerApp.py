from economix_ui_ui import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

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

        self.dashboard_1.click()

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
            self.combobox_organizador.addItem("No Seleccionado")

    def mostar_creacion_de_sub_tabla_sub(self):
        if self.checkbox_suborganizador.isChecked():
            self.combobox_suborganizador.setEnabled(True)
            self.mostrar_hijos_por_organizador()
        else:
            self.combobox_suborganizador.setEnabled(False)
            self.combobox_suborganizador.clear()
            self.combobox_suborganizador.addItem("No Seleccionado")


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
        nombre = self.lineedit_nuevoorganizaor.text()
        if not nombre.strip():
            self.mostrar_error("El nombre del organizador es obligatorio")
            return
        
        organizador_abuelo = None
        organizador_padre = None

        if self.checkbox_organizador.isChecked():
            organizador_abuelo = self.combobox_organizador.currentText()
        
        if self.checkbox_suborganizador.isChecked():
            organizador_padre = self.combobox_suborganizador.currentText()


        if not organizador_abuelo and not organizador_padre:
            self.treeWidget_organizadores.addTopLevelItem(QTreeWidgetItem([nombre]))
            return

        item_abuelo = None
        if organizador_abuelo:
            for i in range(self.treeWidget_organizadores.topLevelItemCount()):
                item = self.treeWidget_organizadores.topLevelItem(i)
                if item.text(0) == organizador_abuelo:
                    item_abuelo = item
                    break

        if organizador_abuelo and not organizador_padre:
            if item_abuelo:
                nuevo_organizador = QTreeWidgetItem([nombre])
                item_abuelo.addChild(nuevo_organizador)
            else:
                print("El organizador no se encontro")
            return

        if organizador_abuelo and organizador_padre:
            if item_abuelo:
                item_padre = None
                for i in range(item_abuelo.childCount()):
                    item = item_abuelo.child(i)
                    if item.text(0) == organizador_padre:
                        item_padre = item
                        break
                
                if item_padre:
                    nuevo_organizador = QTreeWidgetItem([nombre])
                    item_padre.addChild(nuevo_organizador)
                    return

        
    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)
        