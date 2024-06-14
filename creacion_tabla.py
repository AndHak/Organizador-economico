import pandas as pd
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

# Definición de la clase PandasModel que hereda de QAbstractTableModel
class PandasModel(QAbstractTableModel):
    # Método constructor de la clase
    def __init__(self, df=pd.DataFrame(), parent=None):
        # Inicializa la clase base QAbstractTableModel
        QAbstractTableModel.__init__(self, parent)
        # Guarda el DataFrame en un atributo de la clase
        self._data = df  

    # Método para obtener el número de filas del modelo
    def rowCount(self, parent=None):
        # Devuelve el número de filas del DataFrame
        return self._data.shape[0]  

    # Método para obtener el número de columnas del modelo
    def columnCount(self, parent=None):
        # Devuelve el número de columnas del DataFrame
        return self._data.shape[1]  

    # Método para obtener los datos que se mostrarán en la tabla
    def data(self, index, role=Qt.DisplayRole):
        # Verifica si el índice es válido
        if index.isValid():
            # Si el rol es DisplayRole o EditRole, devuelve el valor correspondiente en el DataFrame
            if role == Qt.DisplayRole or role == Qt.EditRole:
                return str(self._data.iloc[index.row(), index.column()])
        # Si no es válido, devuelve None
        return None

    # Método para establecer nuevos datos en la tabla
    def setData(self, index, value, role=Qt.EditRole):
        # Verifica si el índice es válido y si el rol es EditRole
        if index.isValid() and role == Qt.EditRole:
            # Obtiene el nombre de la columna correspondiente al índice
            col_name = self._data.columns[index.column()]
            # Intentar validar y convertir el valor según el tipo de columna
            try:
                if col_name == 'Fecha':
                    # Si la columna es 'Fecha', convierte el valor a datetime con el formato especificado
                    if value.strip() != "":
                        pd.to_datetime(value, format='%d/%m/%Y')
                elif col_name == 'Hora':
                    # Si la columna es 'Hora', convierte el valor a datetime con el formato especificado
                    if value.strip() != "":
                        pd.to_datetime(value, format='%H:%M')
                elif col_name == 'Valor':
                    # Si la columna es 'Valor', convierte el valor a float
                    if value.strip() != "":
                        float(value)
            # Si ocurre un error de conversión, retorna False
            except ValueError:
                return False

            # Si la validación es exitosa, establece el nuevo valor en el DataFrame
            self._data.iloc[index.row(), index.column()] = value
            # Emite la señal dataChanged para notificar a la vista de que los datos han cambiado
            self.dataChanged.emit(index, index, (Qt.DisplayRole, Qt.EditRole))
            return True
        # Si el índice no es válido o el rol no es EditRole, retorna False
        return False

    # Método para obtener los datos del encabezado
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        # Verifica si el rol es DisplayRole
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                # Si la orientación es horizontal, devuelve el nombre de la columna
                return self._data.columns[section]
            elif orientation == Qt.Vertical:
                # Si la orientación es vertical, devuelve el número de fila (sumando 1 para empezar en 1 en lugar de 0)
                return str(section + 1)
        # Si no se cumple ninguna de las condiciones, devuelve None
        return None

    # Método para establecer nuevos datos en los encabezados
    def setHeaderData(self, section, orientation, value, role=Qt.EditRole):
        # Verifica si el rol es EditRole, la orientación es Horizontal y la sección es mayor o igual a 4
        if role == Qt.EditRole and orientation == Qt.Horizontal and section >= 4:
            # Establece el nuevo nombre de la columna
            self._data.columns.values[section] = value
            # Emite la señal headerDataChanged para notificar a la vista de que los encabezados han cambiado
            self.headerDataChanged.emit(orientation, section, section)
            return True
        # Si no se cumple ninguna de las condiciones, retorna False
        return False

    # Método para obtener las banderas de los elementos
    def flags(self, index):
        # Verifica si el índice no es válido
        if not index.isValid():
            # Devuelve las banderas por defecto: seleccionable y habilitado
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        # Si el índice es válido, devuelve las banderas que permiten seleccionar, habilitar y editar el elemento
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable