#temas QTreeWidget, QTreeWidgetItem y QTreeView
#QTableWideget, QTableWidgetItem y QTableView
#QMainWindow, Toolbars and Menus

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from MyOrganizerApp import MyOrganizerApp

app = QApplication(sys.argv)

window = MyOrganizerApp()

window.show()
app.exec()