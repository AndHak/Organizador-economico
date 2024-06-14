from economix_ui_ui import Ui_MainWindow
from creacion_tabla import PandasModel
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import pandas as pd
import sys
import webbrowser
import datetime


class MyOrganizerApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")

        self.hora_timer = QTimer()
        self.hora_timer.timeout.connect(self.actualizar_hora)
        self.hora_timer.start(1000)

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
        self.lineedit_nombretabla.editingFinished.connect(self.actualizar_nombre_tabla_desde_lineedit)


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


        #funciones para el treewidget
        self.agregar_organizador_button.clicked.connect(self.add_category)
        self.agregar_nueva_categoria_button.clicked.connect(self.add_subcategory)
        self.eliminar_organizador_button.clicked.connect(self.remove_item)

        self.toggle_buttons_visibility(False)

        #listas para llevar los nombres de las categorias y subcategorias
        self.categorias = []
        self.subcategorias = []

        #conexiones ayuda del menubar
        self.actionSoporte.triggered.connect(self.switch_to_supportPage)
        self.actionAcerca_De.triggered.connect(self.switch_to_aboutusPage)

        #conexiones archivos menubar
        self.actionSalir.triggered.connect(QApplication.quit)
        self.actionImportar_organizador.triggered.connect(self.import_table)
        self.actionExportar_organizador.triggered.connect(self.exportar_a_excel)

        #conexion botones nueva columna nueva fila y borrar
        self.nueva_fila_button.clicked.connect(self.nueva_fila)
        self.nueva_columna_button.clicked.connect(self.nueva_columna)
        self.eliminar_tabla_button.clicked.connect(self.borrar_fila_o_columna)


    def mostrar_nombres_tablas(self):
        nombres_tablas = list(self.tablas.keys())  # Obtener los nombres de todas las tablas
        model = QStringListModel(nombres_tablas, self)   # Crear un modelo de lista de cadenas
        self.total_gastos_view.setModel(model)      # Asignar el modelo a total_gastos_view
        print("Modelo actualizado con nombres de tablas:", nombres_tablas)  # Verificación

    
    def calcular_valor_total(self):
        total_global = 0
        
        for nombre_tabla, info_tabla in self.tablas.items():
            df = info_tabla['dataframe']
            if 'Valor' in df.columns:
                valores = df['Valor']
                valores_numericos = pd.to_numeric(valores, errors='coerce')
                valores_numericos_validos = valores_numericos.dropna()
                if not valores_numericos_validos.empty:
                    total_tabla = valores_numericos_validos.sum()
                    print(f"Valor total de '{nombre_tabla}': {total_tabla}")
                    total_global += total_tabla
        
        print(f"Valor total global de todas las tablas: {total_global}")

    def exportar_a_excel(self):
        # Obtener el ítem seleccionado actualmente en el treeWidget_organizadores
        selected_item = self.treeWidget_organizadores.currentItem()
        if selected_item:
            nombre_tabla = selected_item.text(0)
            if nombre_tabla in self.tablas:
                # Obtener el dataframe asociado a la tabla seleccionada
                dataframe = self.tablas[nombre_tabla]['dataframe']
                
                # Lógica para exportar el dataframe a Excel
                try:
                    filename, _ = QFileDialog.getSaveFileName(self, "Guardar como...", "", "Excel Files (*.xlsx)")
                    if filename:
                        dataframe.to_excel(filename, index=False)
                        self.mostrar_mensaje(f"Tabla '{nombre_tabla}' exportada exitosamente a {filename}")
                except Exception as e:
                    self.mostrar_mensaje(f"No se pudo exportar la tabla '{nombre_tabla}' a Excel. Error: {str(e)}")
            else:
                self.mostrar_mensaje(f"No se encontró la tabla '{nombre_tabla}'. Seleccione una tabla válida.")
        else:
            self.mostrar_mensaje("No se ha seleccionado ninguna tabla. Seleccione una tabla para exportar a Excel.")
    

    
    def nueva_fila(self):
        # Agregar una nueva fila vacía al DataFrame actual
        if self.current_table_name:
            df = self.tablas[self.current_table_name]['dataframe']
            nueva_fila = pd.DataFrame(['']*len(df.columns), index=df.columns).T
            df = pd.concat([df, nueva_fila], ignore_index=True)
            self.tablas[self.current_table_name]['dataframe'] = df
            self.actualizar_vista_tabla(df)
        else:
            self.mostrar_warning("No hay tabla seleccionada para agregar una fila.")

    def nueva_columna(self):
        # Agregar una nueva columna vacía al DataFrame actual
        if self.current_table_name:
            df = self.tablas[self.current_table_name]['dataframe']
            nueva_columna = f'Columna {len(df.columns) + 1}'
            df[nueva_columna] = ''
            self.tablas[self.current_table_name]['dataframe'] = df
            self.actualizar_vista_tabla(df)
        else:
            self.mostrar_warning("No hay tabla seleccionada para agregar una columna.")

    def borrar_fila(self, indice):
        # Borrar la fila seleccionada del DataFrame actual
        if self.current_table_name:
            df = self.tablas[self.current_table_name]['dataframe']
            df = df.drop(indice, axis=0).reset_index(drop=True)
            self.tablas[self.current_table_name]['dataframe'] = df
            self.actualizar_vista_tabla(df)
        else:
            self.mostrar_warning("No hay tabla seleccionada para borrar una fila.")

    def borrar_columna(self, indice):
        # Borrar la columna seleccionada del DataFrame actual
        if self.current_table_name:
            df = self.tablas[self.current_table_name]['dataframe']
            df = df.drop(df.columns[indice], axis=1)
            self.tablas[self.current_table_name]['dataframe'] = df
            self.actualizar_vista_tabla(df)
        else:
            self.mostrar_warning("No hay tabla seleccionada para borrar una columna.")

    def borrar_fila_o_columna(self):
        # Determinar si borrar una fila o una columna según la selección actual en la tabla
        indices_seleccionados = self.tableView.selectionModel().selectedIndexes()
        if indices_seleccionados:
            filas_seleccionadas = set(indice.row() for indice in indices_seleccionados)
            columnas_seleccionadas = set(indice.column() for indice in indices_seleccionados)
            if len(filas_seleccionadas) == 1 and len(columnas_seleccionadas) == len(self.tablas[self.current_table_name]['dataframe'].columns):
                self.borrar_fila(list(filas_seleccionadas)[0])
            elif len(columnas_seleccionadas) == 1 and len(filas_seleccionadas) == len(self.tablas[self.current_table_name]['dataframe'].index):
                self.borrar_columna(list(columnas_seleccionadas)[0])
            else:
                self.mostrar_warning("Por favor selecciona solo una fila completa o una columna completa para borrar.")
        else:
            self.mostrar_warning("No hay selección para borrar.")

    def actualizar_vista_tabla(self, df):
        # Actualizar la vista de la tabla en la interfaz gráfica
        model = PandasModel(df)
        self.tableView.setModel(model)

    def import_table(self):
        # Abre un cuadro de diálogo para seleccionar el archivo de la tabla
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo", "", "Archivos XLSX (*.xlsx);;Todos los Archivos (*)")
        
        if file_path:
            # Verificar si el archivo seleccionado es una tabla válida
            try:
                df = pd.read_excel(file_path, engine='openpyxl')
            except Exception as e:
                self.mostrar_error(f"Error al cargar el archivo: {str(e)}")
                return

            # Obtener el nombre del archivo sin extensión
            table_name = QFileInfo(file_path).baseName()

            # Verificar si el nombre de la tabla ya existe como categoría o tabla
            if self.is_category_or_table_name(table_name):
                self.mostrar_warning("El nombre de la tabla ya existe como categoría o tabla.")
                return

            # Abrir un cuadro de diálogo para seleccionar la ubicación en el treeWidget
            location_dialog = QDialog(self)
            layout = QVBoxLayout(location_dialog)

            # Agregar los labels y comboboxes
            category_label = QLabel("Categoría:")
            subcategory_label = QLabel("Subcategoría:")
            layout.addWidget(category_label)
            category_combobox = QComboBox()
            category_combobox.addItem("Ninguno")
            layout.addWidget(category_combobox)

            layout.addWidget(subcategory_label)
            subcategory_combobox = QComboBox()
            subcategory_combobox.setEnabled(False)  # Inicialmente deshabilitado
            layout.addWidget(subcategory_combobox)

            # Añadir categorías y subcategorías a los comboboxes
            categories = []
            subcategories = {}

            for i in range(self.treeWidget_organizadores.topLevelItemCount()):
                item = self.treeWidget_organizadores.topLevelItem(i)
                category_name = item.text(0)
                categories.append(category_name)
                subcategories[category_name] = ["Ninguno"]  # Incluye "Ninguno" como opción predeterminada
                for j in range(item.childCount()):
                    subitem = item.child(j)
                    subcategory_name = subitem.text(0)
                    subcategories[category_name].append(subcategory_name)

            category_combobox.addItems(categories)

            def update_subcategories(index):
                selected_category = category_combobox.currentText()
                if selected_category == "Ninguno":
                    subcategory_combobox.clear()
                    subcategory_combobox.addItem("Ninguno")
                    subcategory_combobox.setEnabled(False)
                else:
                    subcategory_combobox.clear()
                    subcategory_combobox.addItems(subcategories[selected_category])
                    subcategory_combobox.setEnabled(True)

            category_combobox.currentIndexChanged.connect(update_subcategories)
            update_subcategories(0)  # Para asegurar que las subcategorías se actualicen correctamente al inicio

            # Botones de Aceptar y Cancelar
            buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, location_dialog)
            buttons.accepted.connect(location_dialog.accept)
            buttons.rejected.connect(location_dialog.reject)
            layout.addWidget(buttons)

            location_dialog.setLayout(layout)

            if location_dialog.exec() == QDialog.Accepted:
                selected_category = category_combobox.currentText()
                selected_subcategory = subcategory_combobox.currentText()

                # Lógica para agregar la tabla en la ubicación correcta
                if selected_category == "Ninguno":
                    # Agregar fuera de categorías
                    selected_item = None
                else:
                    # Buscar la ubicación en el treeWidget
                    for i in range(self.treeWidget_organizadores.topLevelItemCount()):
                        item = self.treeWidget_organizadores.topLevelItem(i)
                        if item.text(0) == selected_category:
                            selected_item = item
                            if selected_subcategory != "Ninguno":
                                for j in range(item.childCount()):
                                    subitem = item.child(j)
                                    if subitem.text(0) == selected_subcategory:
                                        selected_item = subitem
                                        break
                            break
                    else:
                        self.mostrar_error("Ubicación no encontrada en el árbol de organizadores.")
                        return

                # Añadir la nueva tabla a la estructura y actualizar el treeWidget
                self.add_table_to_location(df, table_name, selected_item)  # Llama al método para agregar la tabla

    def is_category_or_table_name(self, name):
        # Verifica si el nombre ya existe como categoría o tabla en el árbol de organizadores
        for i in range(self.treeWidget_organizadores.topLevelItemCount()):
            item = self.treeWidget_organizadores.topLevelItem(i)
            if item.text(0) == name:
                return True  # Nombre existe como categoría
            for j in range(item.childCount()):
                subitem = item.child(j)
                if subitem.text(0) == name:
                    return True  # Nombre existe como subcategoría
        return False  # Nombre no existe como categoría ni subcategoría

    def add_table_to_location(self, table, table_name, selected_item=None):
        # Añadir la nueva tabla a la estructura y actualizar el treeWidget
        self.tablas[table_name] = {'dataframe': table, 'color': self.selected_color}
        new_table_item = QTreeWidgetItem([table_name])

        if selected_item:
            selected_item.addChild(new_table_item)
        else:
            self.treeWidget_organizadores.addTopLevelItem(new_table_item)

        self.mostrar_tabla_seleccionada()  # Mostrar la tabla recién añadida






        

    def actualizar_hora(self):
        hora_actual = datetime.datetime.now().strftime("%I:%M %p")
        self.label_9.setText(hora_actual)

    
    def toggle_buttons_visibility(self, visible):
        # Cambiar el estado de visibilidad de los botones basado en el parámetro visible
        self.agregar_organizador_button.setVisible(visible)
        self.agregar_nueva_categoria_button.setVisible(visible)
        self.eliminar_organizador_button.setVisible(visible)
        self.nueva_fila_button.setVisible(visible)
        self.nueva_columna_button.setVisible(visible)


    def add_category(self):
        # Abrir un QInputDialog para recoger el nombre de la categoría
        category_name, ok = QInputDialog.getText(self, "Añadir Categoria:", "Nombre de la Categoria")
        
        if ok and category_name is not None:  # Verificar si se hizo clic en OK y category_name no es None
            category_name = category_name.strip()  # Eliminar espacios en blanco al inicio y final
            
            if category_name:  # Verificar si el nombre no está vacío después de quitar espacios en blanco
                if category_name not in self.categorias:
                    # Crear un nuevo QTreeWidgetItem con el nombre de la categoría
                    new_category = QTreeWidgetItem([category_name])
                    # Añadir el nuevo QTreeWidgetItem al QTreeWidget
                    self.treeWidget_organizadores.addTopLevelItem(new_category)
                    # Agregar la categoría a la lista de categorías
                    self.categorias.append(category_name)
                else:
                    self.mostrar_warning("El nombre ya existe en las Categorias, favor digite uno distinto")
            else:
                self.mostrar_warning("El nombre de la Categoria no debe estar vacio")

                
    
    def add_subcategory(self):
        # Obtener la categoría seleccionada
        selected_item = self.treeWidget_organizadores.currentItem()
        
        if not selected_item:
            self.mostrar_warning("Para añadir una SubCategoría primero debe seleccionar una Categoría")
            return
        
        # Comprobar si el item seleccionado ya es una subcategoría
        if selected_item.parent():
            self.mostrar_warning("No se puede añadir una SubCategoría a una SubCategoría")
        else:
            # Abrir un QInputDialog para recoger el nombre de la subcategoría
            subcategory_name, ok = QInputDialog.getText(self, "Añadir SubCategoría", "Nombre de la SubCategoría:")
            
            if ok and subcategory_name is not None:  # Verificar si se hizo clic en OK y subcategory_name no es None
                subcategory_name = subcategory_name.strip()  # Eliminar espacios en blanco al inicio y final
                
                if subcategory_name:  # Verificar si el nombre no está vacío después de quitar espacios en blanco
                    if subcategory_name not in self.subcategorias:
                        # Crear un nuevo QTreeWidgetItem con el nombre de la subcategoría
                        new_subcategory = QTreeWidgetItem([subcategory_name])
                        # Añadir el nuevo QTreeWidgetItem como hijo de la categoría seleccionada
                        selected_item.addChild(new_subcategory)
                        # Agregar la subcategoría a la lista de subcategorías
                        self.subcategorias.append(subcategory_name)
                    else:
                        self.mostrar_warning("El nombre ya existe en las SubCategorías, favor digite uno distinto")
                else:
                    self.mostrar_warning("El nombre de la SubCategoría no debe estar vacío")

                       
    
    def remove_item(self):
        # Obtener el item seleccionado
        selected_item = self.treeWidget_organizadores.currentItem()
        
        if not selected_item:
            self.mostrar_warning("Para eliminar un Item de su lista primero debe seleccionarlo")
            return
        else:
            # Preguntar al usuario si realmente quiere eliminar el item seleccionado
            reply = QMessageBox.question(self, '¿Eliminar Item?', '¿Está seguro de que quiere eliminar este item?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                # Eliminar el item seleccionado y sus tablas asociadas
                self.eliminar_item_y_tablas(selected_item)
                
                # Limpiar la vista de la tabla y el lineedit_nombretabla
                self.limpiar_vista_tabla()

    def eliminar_item_y_tablas(self, item):
        # Verificar si el item tiene hijos
        while item.childCount() > 0:
            child = item.takeChild(0)
            self.eliminar_item_y_tablas(child)
        
        # Si el item tiene un nombre de tabla, eliminarlo de self.tablas
        nombre_tabla = item.text(0)
        if nombre_tabla in self.tablas:
            del self.tablas[nombre_tabla]
        
        # Eliminar el item del árbol
        parent = item.parent()
        if parent is None:
            self.treeWidget_organizadores.takeTopLevelItem(self.treeWidget_organizadores.indexOfTopLevelItem(item))
        else:
            parent.removeChild(item)

    def limpiar_vista_tabla(self):
        # Limpiar el lineedit_nombretabla
        if hasattr(self, 'lineedit_nombretabla'):
            self.lineedit_nombretabla.clear()
            self.lineedit_nombretabla.setStyleSheet("")

        # Limpiar la vista de la tabla
        self.tableView.setModel(None)
        #desactiva los desencadenadores de edición en el QTableView, asegurando que la tabla no sea editable.
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    
    def limpiar_nuevo_organizador_page(self):
        self.combobox_organizador.clear()
        self.combobox_suborganizador.clear()
        self.lineedit_nuevoorganizaor.clear()
        self.spinbox_columnas.clear()
        self.spinbox_filas.clear()

    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentWidget(self.Dashboard_page)
        self.limpiar_nuevo_organizador_page()
        self.mostrar_nombres_tablas()
        self.calcular_valor_total()

    def switch_to_newPage(self):
        self.stackedWidget.setCurrentWidget(self.nuevo_organizador_page)
        self.limpiar_nuevo_organizador_page()
        

    def switch_to_supportPage(self):
        self.stackedWidget.setCurrentWidget(self.suppot_page)
        self.limpiar_nuevo_organizador_page()
        

    def switch_to_aboutusPage(self):
        self.stackedWidget.setCurrentWidget(self.about_us_page)
        self.limpiar_nuevo_organizador_page()
        

    def switch_to_settingsPage(self):
        self.stackedWidget.setCurrentWidget(self.Settings_page)
        self.limpiar_nuevo_organizador_page()
        

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
        
        if nombre in self.tablas:
            self.mostrar_error("Ya existe una tabla con ese nombre.")
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
        filas = 5  # Número de filas por defecto
        columnas_adicionales = int(self.spinbox_columnas.value())
        columnas_fijas = ['Descripción', 'Fecha', 'Hora', 'Valor']
        columnas_nombres = columnas_fijas + [f'Columna {i+1}' for i in range(columnas_adicionales)]
        
        # Crear un DataFrame de pandas con la cabecera fija y el número especificado de filas
        return pd.DataFrame('', index=range(1, filas+1), columns=columnas_nombres)



    def mostrar_tabla_seleccionada(self):
        selected_item = self.treeWidget_organizadores.currentItem()
        if selected_item:
            nombre_tabla = selected_item.text(0)
            if nombre_tabla in self.tablas:
                self.current_table_name = nombre_tabla  # Actualizar el nombre de la tabla actual
                
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
                self.mostrar_nombres_tablas()
                self.calcular_valor_total()

                # Configurar el modo de edición según el estado del botón
                if self.edit_save_button.text() == "Guardar":
                    self.tableView.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)
                else:
                    self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def edit_all(self):
        if self.edit_save_button.text() == "Editar":
            self.toggle_buttons_visibility(True)
            self.edit_save_button.setText("Guardar")
            self.treeWidget_organizadores.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)
            self.tableView.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)
            self.lineedit_nombretabla.setReadOnly(False)
        else:
            if self.validar_datos():
                nuevo_nombre = self.lineedit_nombretabla.text().strip()
                if nuevo_nombre:
                    self.actualizar_nombre_tabla_desde_lineedit()
                self.lineedit_nombretabla.setReadOnly(True)
                self.edit_save_button.setText("Editar")
                self.toggle_buttons_visibility(False)
                self.treeWidget_organizadores.setEditTriggers(QAbstractItemView.NoEditTriggers)
                self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
            else:
                self.mostrar_error("Hay errores en los datos. Por favor, corrígelos antes de guardar.")


    def validar_datos(self):
        model = self.tableView.model()
        if model:
            for row in range(model.rowCount()):
                for col in range(model.columnCount()):
                    index = model.index(row, col)
                    col_name = model._data.columns[col]
                    value = model.data(index, Qt.EditRole).strip()
                    if col_name == 'Valor':
                        if value:
                            try:
                                float(value)
                            except ValueError:
                                return False  # Valor no es un número
                    elif col_name == 'Fecha':
                        if value:
                            try:
                                pd.to_datetime(value, format='%d/%m/%Y')
                            except ValueError:
                                return False  # Fecha no válida
                    elif col_name == 'Hora':
                        if value:
                            try:
                                pd.to_datetime(value, format='%H:%M')
                            except ValueError:
                                return False  # Hora no válida
        return True

    def actualizar_nombre_tabla_desde_lineedit(self):
        nuevo_nombre = self.lineedit_nombretabla.text().strip()
        if not nuevo_nombre:
            self.mostrar_error("El nombre del organizador no puede estar vacío.")
            self.mostrar_tabla_seleccionada()  # Restaurar el nombre anterior en el line edit
            return False

        selected_item = self.treeWidget_organizadores.currentItem()
        if selected_item:
            nombre_antiguo = selected_item.text(0)

            if nuevo_nombre in self.tablas and nuevo_nombre != nombre_antiguo:
                self.mostrar_error("Ya existe una tabla con ese nombre.")
                self.mostrar_tabla_seleccionada()  # Restaurar el nombre anterior en el line edit
                return False

            if nombre_antiguo in self.tablas:
                # Actualiza el nombre en el tree widget
                selected_item.setText(0, nuevo_nombre)
                selected_item.setData(0, Qt.UserRole, nuevo_nombre)
                
                # Actualiza el diccionario tablas
                self.tablas[nuevo_nombre] = self.tablas.pop(nombre_antiguo)

                # Actualiza el combobox de organizadores
                self.actualizar_combobox_organizadores()
                return True
            else:
                self.mostrar_error(f"El nombre antiguo '{nombre_antiguo}' no se encontró en las tablas.")
                self.mostrar_tabla_seleccionada()  # Restaurar el nombre anterior en el line edit
                return False

        self.mostrar_error("No hay ningún ítem seleccionado.")
        return False


    def actualizar_nombre_organizador(self, item, column):
        nuevo_nombre = item.text(column).strip()
        nombre_antiguo = item.data(column, Qt.UserRole)

        if nombre_antiguo and nuevo_nombre:
            if nuevo_nombre in self.tablas and nuevo_nombre != nombre_antiguo:
                self.mostrar_error("Ya existe una tabla con ese nombre.")
                item.setText(column, nombre_antiguo)
                return

            if nombre_antiguo in self.tablas:
                self.tablas[nuevo_nombre] = self.tablas.pop(nombre_antiguo)
                item.setData(column, Qt.UserRole, nuevo_nombre)

                if self.lineedit_nombretabla.text() == nombre_antiguo:
                    self.lineedit_nombretabla.setText(nuevo_nombre)
            else:
                self.mostrar_error("El nombre antiguo no se encontró en las tablas.")
                item.setText(column, nombre_antiguo)
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

    def enviar_correo(self):
        seleccionado = self.list_apoyo.currentItem()
        texto = self.plainTextEdit_support.toPlainText().strip()
        texto_a_enviar = self.plainTextEdit_support.toPlainText()

        if seleccionado:
            asunto = seleccionado.text()
            if texto:
                destinatario = "afmartinez23a@udenar.edu.co"
                # Crear el enlace mailto
                mailto_link = f"mailto:{destinatario}?subject={asunto}&body={texto_a_enviar}"

                mailto_link = mailto_link.replace(' ', '%20')

                # Abrir el enlace en el navegador predeterminado
                webbrowser.open(mailto_link)
                self.plainTextEdit_support.clear()

            else:
                self.mostrar_warning("El texto del recuadro inferior no debe estar vacio")
        else:
            self.mostrar_warning("Debes seleccionar un asunto de la lista")
    
    def mostrar_warning(self, message):
        QMessageBox.warning(self, "Advertencia", message)

    def mostrar_mensaje(self, message):
        QMessageBox.information(self, "Informacion", message)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("windowsvista")
    window = MyOrganizerApp()

    window.show()
    app.exec()
