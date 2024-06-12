import pandas as pd
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class PandasModel(QAbstractTableModel):
    def __init__(self, columnas, filas, df=pd.DataFrame(), parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = df

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole or role == Qt.EditRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            col_name = self._data.columns[index.column()]
            try:
                if col_name == 'Fecha':
                    pd.to_datetime(value)  # Validar fecha
                elif col_name == 'Hora':
                    pd.to_datetime(value, format='%H:%M')  # Validar hora
                elif col_name == 'Valor':
                    int(value)  
            except ValueError:
                return False

            self._data.iloc[index.row(), index.column()] = value
            self.dataChanged.emit(index, index, (Qt.DisplayRole, Qt.EditRole))
            return True
        return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._data.columns[section]
            elif orientation == Qt.Vertical:
                return str(section + 1)
        if role == Qt.EditRole and orientation == Qt.Horizontal and section >= 4:
            return self._data.columns[section]
        return None

    def setHeaderData(self, section, orientation, value, role=Qt.EditRole):
        if role == Qt.EditRole and orientation == Qt.Horizontal and section >= 4:
            self._data.columns.values[section] = value
            self.headerDataChanged.emit(orientation, section, section)
            return True
        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        col_name = self._data.columns[index.column()]
        if col_name in ['Descripción', 'Fecha', 'Hora', 'Valor']:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable