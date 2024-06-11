import pandas as pd
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class PandasModel(QAbstractTableModel):
    def __init__(self, df=pd.DataFrame(), parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = df

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
            elif role == Qt.EditRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid():
            if role == Qt.EditRole:
                self._data.iloc[index.row(), index.column()] = value
                self.dataChanged.emit(index, index)
                return True
        return False

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable