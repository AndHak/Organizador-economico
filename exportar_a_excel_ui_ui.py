# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exportar_a_excel_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(733, 422)
        self.enviar_buttton_apoyo = QPushButton(Dialog)
        self.enviar_buttton_apoyo.setObjectName(u"enviar_buttton_apoyo")
        self.enviar_buttton_apoyo.setGeometry(QRect(480, 350, 200, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enviar_buttton_apoyo.sizePolicy().hasHeightForWidth())
        self.enviar_buttton_apoyo.setSizePolicy(sizePolicy)
        self.enviar_buttton_apoyo.setMinimumSize(QSize(200, 50))
        self.enviar_buttton_apoyo.setMaximumSize(QSize(110, 40))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.enviar_buttton_apoyo.setFont(font)
        self.enviar_buttton_apoyo.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviar_buttton_apoyo.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(103, 178, 98, 180); \n"
"    font-size: 17px;\n"
"    padding: 15px;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(103, 178, 98, 150);\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(103, 178, 98, 200);\n"
"    font-size: 18px;\n"
"    border: none;\n"
"}\n"
"")
        self.enviar_buttton_apoyo.setCheckable(True)
        self.enviar_buttton_apoyo_2 = QPushButton(Dialog)
        self.enviar_buttton_apoyo_2.setObjectName(u"enviar_buttton_apoyo_2")
        self.enviar_buttton_apoyo_2.setGeometry(QRect(260, 350, 200, 50))
        sizePolicy.setHeightForWidth(self.enviar_buttton_apoyo_2.sizePolicy().hasHeightForWidth())
        self.enviar_buttton_apoyo_2.setSizePolicy(sizePolicy)
        self.enviar_buttton_apoyo_2.setMinimumSize(QSize(200, 50))
        self.enviar_buttton_apoyo_2.setMaximumSize(QSize(110, 40))
        self.enviar_buttton_apoyo_2.setFont(font)
        self.enviar_buttton_apoyo_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviar_buttton_apoyo_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(250, 82, 82, 150);\n"
"    font-size: 17px;\n"
"    padding: 15px;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(103, 178, 98, 150);\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(103, 178, 98, 200);\n"
"    font-size: 18px;\n"
"    border: none;\n"
"}\n"
"")
        self.enviar_buttton_apoyo_2.setCheckable(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.enviar_buttton_apoyo.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.enviar_buttton_apoyo_2.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

