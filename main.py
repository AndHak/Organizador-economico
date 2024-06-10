


from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from dashboard import MySideBar

app = QApplication(sys.argv)

window = MySideBar()

window.show()
app.exec()