# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'economix_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTabWidget, QTableView,
    QTextBrowser, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import recurses_rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.actionExportar_organizador = QAction(MainWindow)
        self.actionExportar_organizador.setObjectName(u"actionExportar_organizador")
        self.actionImportar_organizador = QAction(MainWindow)
        self.actionImportar_organizador.setObjectName(u"actionImportar_organizador")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionAcerca_De = QAction(MainWindow)
        self.actionAcerca_De.setObjectName(u"actionAcerca_De")
        self.actionSoporte = QAction(MainWindow)
        self.actionSoporte.setObjectName(u"actionSoporte")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget {\n"
"	background-color: #67b262;\n"
"}\n"
"QPushButton {\n"
"	color: white;\n"
"	height: 50px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(245, 250, 254);\n"
"	color: rgb(105, 185, 255);\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, 20)
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setPixmap(QPixmap(u":/icons/Images/logo.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        self.dashboard_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/Images/dashboard_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/Images/dashboard.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setIconSize(QSize(40, 40))
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.new_1_button = QPushButton(self.icon_only_widget)
        self.new_1_button.setObjectName(u"new_1_button")
        self.new_1_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Images/new_organizer_white.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/Images/new_organizer.png", QSize(), QIcon.Normal, QIcon.On)
        self.new_1_button.setIcon(icon1)
        self.new_1_button.setIconSize(QSize(40, 40))
        self.new_1_button.setCheckable(True)
        self.new_1_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.new_1_button)

        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        self.settings_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Images/icons8-setting-50.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/Images/icons8-setting-50 (1).png", QSize(), QIcon.Normal, QIcon.On)
        self.settings_1.setIcon(icon2)
        self.settings_1.setIconSize(QSize(40, 40))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 315, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.singout_1 = QPushButton(self.icon_only_widget)
        self.singout_1.setObjectName(u"singout_1")
        self.singout_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/Images/icons8-off-91.png", QSize(), QIcon.Normal, QIcon.Off)
        self.singout_1.setIcon(icon3)
        self.singout_1.setIconSize(QSize(40, 40))
        self.singout_1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.singout_1)


        self.horizontalLayout_7.addWidget(self.icon_only_widget)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget {\n"
"	background-color: #67b262;\n"
"	color: white;\n"
"}\n"
"QPushButton {\n"
"	color: white;\n"
"	text-align:left;\n"
"	height: 50px;\n"
"	font-size: 15px;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(245, 250, 254);\n"
"	color:  #67b262;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 20, 0, 20)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 60))
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setPixmap(QPixmap(u":/icons/Images/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_name_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setIconSize(QSize(40, 40))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.new_2_button = QPushButton(self.icon_name_widget)
        self.new_2_button.setObjectName(u"new_2_button")
        self.new_2_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_2_button.setIcon(icon1)
        self.new_2_button.setIconSize(QSize(40, 40))
        self.new_2_button.setCheckable(True)
        self.new_2_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.new_2_button)

        self.settings_2 = QPushButton(self.icon_name_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_2.setIcon(icon2)
        self.settings_2.setIconSize(QSize(40, 40))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 313, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.singout_2 = QPushButton(self.icon_name_widget)
        self.singout_2.setObjectName(u"singout_2")
        self.singout_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.singout_2.setIcon(icon3)
        self.singout_2.setIconSize(QSize(40, 40))
        self.singout_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.singout_2)


        self.horizontalLayout_7.addWidget(self.icon_name_widget)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.main_menu)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.menu = QPushButton(self.widget)
        self.menu.setObjectName(u"menu")
        self.menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu.setStyleSheet(u"border: none;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Images/icons8-menu-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon4)
        self.menu.setIconSize(QSize(40, 40))
        self.menu.setCheckable(True)

        self.gridLayout_4.addWidget(self.menu, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(275, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(275, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAcceptDrops(True)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Dashboard_page = QWidget()
        self.Dashboard_page.setObjectName(u"Dashboard_page")
        self.gridLayout_9 = QGridLayout(self.Dashboard_page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(15)
        self.gridLayout_9.setContentsMargins(20, 20, 20, 20)
        self.label_10 = QLabel(self.Dashboard_page)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setFamilies([u"Malgun Gothic"])
        font1.setBold(True)
        font1.setItalic(False)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"font-size: 30px;")
        self.label_10.setLocale(QLocale(QLocale.Spanish, QLocale.Colombia))

        self.gridLayout_9.addWidget(self.label_10, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.Dashboard_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 933, 461))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.agregar_organizador_button = QPushButton(self.scrollAreaWidgetContents)
        self.agregar_organizador_button.setObjectName(u"agregar_organizador_button")
        self.agregar_organizador_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.agregar_organizador_button.setStyleSheet(u"border: none;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Images/icons8-plus-math-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar_organizador_button.setIcon(icon5)
        self.agregar_organizador_button.setIconSize(QSize(30, 30))
        self.agregar_organizador_button.setCheckable(True)
        self.agregar_organizador_button.setAutoExclusive(False)

        self.gridLayout.addWidget(self.agregar_organizador_button, 1, 4, 1, 1)

        self.agregar_nueva_categoria_button = QPushButton(self.scrollAreaWidgetContents)
        self.agregar_nueva_categoria_button.setObjectName(u"agregar_nueva_categoria_button")
        self.agregar_nueva_categoria_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.agregar_nueva_categoria_button.setStyleSheet(u"border: none;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Images/icons8-new-folder-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.agregar_nueva_categoria_button.setIcon(icon6)
        self.agregar_nueva_categoria_button.setIconSize(QSize(30, 30))
        self.agregar_nueva_categoria_button.setCheckable(True)
        self.agregar_nueva_categoria_button.setAutoExclusive(False)

        self.gridLayout.addWidget(self.agregar_nueva_categoria_button, 1, 2, 1, 1)

        self.tab_widget = QTabWidget(self.scrollAreaWidgetContents)
        self.tab_widget.setObjectName(u"tab_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy)
        self.tab_widget.setSizeIncrement(QSize(0, 0))
        self.tab_widget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid #bdbdbd;\n"
"    background: #f5f5f5;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: rgba(103, 178, 98, 100);\n"
"    border: 1px solid #bdbdbd;\n"
"    padding: 10px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    color: #333333;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgba(103, 178, 98, 200);\n"
"    border-color: #b0bec5;\n"
"    color: black;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: rgba(103, 178, 98, 180);\n"
"    color: black;;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 3px; \n"
"}\n"
"\n"
"QTabBar::tab:selected:hover {\n"
"    background: rgba(103, 178, 98, 220);\n"
"    color: black;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.tab_widget.setDocumentMode(False)
        self.tab_widget.setTabsClosable(False)
        self.tab_widget.setMovable(False)
        self.tab_seleccted = QWidget()
        self.tab_seleccted.setObjectName(u"tab_seleccted")
        self.gridLayout_6 = QGridLayout(self.tab_seleccted)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(15, 15, 15, 15)
        self.lineedit_nombretabla = QLineEdit(self.tab_seleccted)
        self.lineedit_nombretabla.setObjectName(u"lineedit_nombretabla")
        self.lineedit_nombretabla.setEnabled(True)
        self.lineedit_nombretabla.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(103, 178, 98); /* Color de fondo */\n"
"    border-top-left-radius: 20px; /* Radio de borde superior izquierdo */\n"
"    border-top-right-radius: 20px; /* Radio de borde superior derecho */\n"
"    font-size: 20px; /* Tama\u00f1o de fuente */\n"
"    font-weight: bold; /* Peso de la fuente */\n"
"    padding: 8px 20px; /* Espaciado dentro del line edit */\n"
"    color: white; /* Color del texto */\n"
"    border: 1px solid gray; /* Borde del line edit */\n"
"}\n"
"")
        self.lineedit_nombretabla.setMaxLength(30)
        self.lineedit_nombretabla.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineedit_nombretabla, 0, 0, 1, 1)

        self.tableView = QTableView(self.tab_seleccted)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_6.addWidget(self.tableView, 1, 0, 1, 1)

        self.tab_widget.addTab(self.tab_seleccted, "")
        self.tab_total = QWidget()
        self.tab_total.setObjectName(u"tab_total")
        self.gridLayout_7 = QGridLayout(self.tab_total)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(15, 15, 15, 15)
        self.total_gastos_view = QListView(self.tab_total)
        self.total_gastos_view.setObjectName(u"total_gastos_view")

        self.gridLayout_7.addWidget(self.total_gastos_view, 0, 0, 1, 1)

        self.tab_widget.addTab(self.tab_total, "")

        self.gridLayout.addWidget(self.tab_widget, 0, 5, 2, 1)

        self.treeWidget_organizadores = QTreeWidget(self.scrollAreaWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget_organizadores)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget_organizadores)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4 = QTreeWidgetItem(self.treeWidget_organizadores)
        QTreeWidgetItem(__qtreewidgetitem4)
        self.treeWidget_organizadores.setObjectName(u"treeWidget_organizadores")
        self.treeWidget_organizadores.setStyleSheet(u"QTreeView {\n"
"    background-color: #ffffff;\n"
"    alternate-background-color: rgba(103, 178, 98, 50); /* Color de fondo alternativo */\n"
"    border: 1px solid #bdbdbd;\n"
"    selection-background-color: rgba(103, 178, 98, 150); /* Color de fondo de la selecci\u00f3n */\n"
"    selection-color: #ffffff; /* Color del texto seleccionado */\n"
"}\n"
"\n"
"QTreeView::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background-color: rgba(103, 178, 98, 100); /* Color de fondo al pasar el cursor */\n"
"    color: black; /* Color del texto al pasar el cursor */\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    background-color: rgba(103, 178, 98, 200); /* Color de fondo de la selecci\u00f3n */\n"
"    color: black; /* Color del texto seleccionado */\n"
"    font-size: 16px !important; /* Importante para asegurar que se aplique */\n"
"    font-weight: bold !important; /* Importante para asegurar que se aplique */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #dcdcdc;"
                        " /* Color de fondo del encabezado */\n"
"    color: #333333; /* Color del texto del encabezado */\n"
"    padding: 4px;\n"
"    border: 1px solid #bdbdbd;\n"
"    font-weight: bold; /* Texto en negrita */\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.treeWidget_organizadores, 0, 0, 1, 5)

        self.eliminar_organizador_button = QPushButton(self.scrollAreaWidgetContents)
        self.eliminar_organizador_button.setObjectName(u"eliminar_organizador_button")
        self.eliminar_organizador_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.eliminar_organizador_button.setStyleSheet(u"border: none;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Images/icons8-subtract-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eliminar_organizador_button.setIcon(icon7)
        self.eliminar_organizador_button.setIconSize(QSize(30, 30))
        self.eliminar_organizador_button.setCheckable(True)
        self.eliminar_organizador_button.setAutoExclusive(False)

        self.gridLayout.addWidget(self.eliminar_organizador_button, 1, 3, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_9.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.eliminar_tabla_button = QPushButton(self.Dashboard_page)
        self.eliminar_tabla_button.setObjectName(u"eliminar_tabla_button")
        self.eliminar_tabla_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.eliminar_tabla_button.setStyleSheet(u"border: none;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Images/icons8-trash-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eliminar_tabla_button.setIcon(icon8)
        self.eliminar_tabla_button.setIconSize(QSize(40, 40))
        self.eliminar_tabla_button.setCheckable(True)
        self.eliminar_tabla_button.setAutoExclusive(False)

        self.horizontalLayout_3.addWidget(self.eliminar_tabla_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.nueva_columna_button = QPushButton(self.Dashboard_page)
        self.nueva_columna_button.setObjectName(u"nueva_columna_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nueva_columna_button.sizePolicy().hasHeightForWidth())
        self.nueva_columna_button.setSizePolicy(sizePolicy1)
        self.nueva_columna_button.setMinimumSize(QSize(200, 50))
        self.nueva_columna_button.setMaximumSize(QSize(110, 40))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setBold(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.nueva_columna_button.setFont(font2)
        self.nueva_columna_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.nueva_columna_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(103, 178, 98, 180); \n"
"    font-size: 17px;\n"
"    padding: 10px;\n"
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
        self.nueva_columna_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.nueva_columna_button)

        self.nueva_fila_button = QPushButton(self.Dashboard_page)
        self.nueva_fila_button.setObjectName(u"nueva_fila_button")
        sizePolicy1.setHeightForWidth(self.nueva_fila_button.sizePolicy().hasHeightForWidth())
        self.nueva_fila_button.setSizePolicy(sizePolicy1)
        self.nueva_fila_button.setMinimumSize(QSize(200, 50))
        self.nueva_fila_button.setMaximumSize(QSize(110, 40))
        self.nueva_fila_button.setFont(font2)
        self.nueva_fila_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.nueva_fila_button.setStyleSheet(u"QPushButton {\n"
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
        self.nueva_fila_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.nueva_fila_button)

        self.edit_save_button = QPushButton(self.Dashboard_page)
        self.edit_save_button.setObjectName(u"edit_save_button")
        sizePolicy1.setHeightForWidth(self.edit_save_button.sizePolicy().hasHeightForWidth())
        self.edit_save_button.setSizePolicy(sizePolicy1)
        self.edit_save_button.setMinimumSize(QSize(200, 50))
        self.edit_save_button.setMaximumSize(QSize(110, 40))
        self.edit_save_button.setFont(font2)
        self.edit_save_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_save_button.setStyleSheet(u"QPushButton {\n"
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
        self.edit_save_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.edit_save_button)


        self.gridLayout_9.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.Dashboard_page)
        self.nuevo_organizador_page = QWidget()
        self.nuevo_organizador_page.setObjectName(u"nuevo_organizador_page")
        self.nuevo_organizador_page.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #bdbdbd;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #a0a0a0;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #bdbdbd;\n"
"    selection-background-color: #b0bec5;\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #bdbdbd;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #a0a0a0;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #78909c;\n"
"    background-color: #f0f4f7;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #bdbdbd;\n"
"    border-radius: 4px;\n"
""
                        "    padding: 4px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_11 = QGridLayout(self.nuevo_organizador_page)
        self.gridLayout_11.setSpacing(20)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_12 = QLabel(self.nuevo_organizador_page)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_11.addWidget(self.label_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(25)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.pushButton_4 = QPushButton(self.nuevo_organizador_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(40, 40))
        self.pushButton_4.setMaximumSize(QSize(40, 40))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(103, 178, 98);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:checked {\n"
"	border: 2px solid black;\n"
"}")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(True)
        self.pushButton_4.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.nuevo_organizador_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(40, 40))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 170, 0);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:checked {\n"
"	border: 2px solid black;\n"
"}")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.pushButton_2, 0, Qt.AlignLeft)

        self.pushButton = QPushButton(self.nuevo_organizador_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 40))
        self.pushButton.setMaximumSize(QSize(40, 40))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 0, 255);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:checked {\n"
"	border: 2px solid black;\n"
"}")
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.pushButton_3 = QPushButton(self.nuevo_organizador_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 40))
        self.pushButton_3.setMaximumSize(QSize(40, 40))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:checked {\n"
"	border: 2px solid black;\n"
"}")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.pushButton_3, 0, Qt.AlignLeft)

        self.pushButton_5 = QPushButton(self.nuevo_organizador_page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(40, 40))
        self.pushButton_5.setMaximumSize(QSize(40, 40))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 85, 0);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:checked {\n"
"	border: 2px solid black;\n"
"}")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.pushButton_5, 0, Qt.AlignLeft)

        self.pushButton_6 = QPushButton(self.nuevo_organizador_page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(40, 40))
        self.pushButton_6.setMaximumSize(QSize(40, 40))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 170, 255);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:checked {\n"
"	border: 2px solid black;\n"
"}")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.pushButton_6, 0, Qt.AlignLeft)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)


        self.gridLayout_11.addLayout(self.verticalLayout_11, 4, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.nuevo_organizador_page)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_10.addWidget(self.label_4)

        self.lineedit_nuevoorganizaor = QLineEdit(self.nuevo_organizador_page)
        self.lineedit_nuevoorganizaor.setObjectName(u"lineedit_nuevoorganizaor")
        self.lineedit_nuevoorganizaor.setMinimumSize(QSize(0, 35))

        self.verticalLayout_10.addWidget(self.lineedit_nuevoorganizaor)


        self.gridLayout_11.addLayout(self.verticalLayout_10, 2, 0, 1, 1)

        self.label_11 = QLabel(self.nuevo_organizador_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"font-size: 30px;")
        self.label_11.setLocale(QLocale(QLocale.Spanish, QLocale.Colombia))

        self.gridLayout_11.addWidget(self.label_11, 0, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 107, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_8, 5, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkbox_organizador = QCheckBox(self.nuevo_organizador_page)
        self.checkbox_organizador.setObjectName(u"checkbox_organizador")

        self.verticalLayout_8.addWidget(self.checkbox_organizador)

        self.combobox_organizador = QComboBox(self.nuevo_organizador_page)
        self.combobox_organizador.setObjectName(u"combobox_organizador")
        self.combobox_organizador.setEnabled(False)
        self.combobox_organizador.setMinimumSize(QSize(0, 35))
        self.combobox_organizador.setEditable(False)

        self.verticalLayout_8.addWidget(self.combobox_organizador)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkbox_suborganizador = QCheckBox(self.nuevo_organizador_page)
        self.checkbox_suborganizador.setObjectName(u"checkbox_suborganizador")

        self.verticalLayout_9.addWidget(self.checkbox_suborganizador)

        self.combobox_suborganizador = QComboBox(self.nuevo_organizador_page)
        self.combobox_suborganizador.setObjectName(u"combobox_suborganizador")
        self.combobox_suborganizador.setEnabled(False)
        self.combobox_suborganizador.setMinimumSize(QSize(0, 35))
        self.combobox_suborganizador.setEditable(False)

        self.verticalLayout_9.addWidget(self.combobox_suborganizador)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)


        self.gridLayout_11.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.nuevo_organizador_page)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_10 = QGridLayout(self.groupBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.checkbox_valor = QCheckBox(self.groupBox)
        self.checkbox_valor.setObjectName(u"checkbox_valor")
        self.checkbox_valor.setEnabled(False)
        self.checkbox_valor.setCheckable(True)
        self.checkbox_valor.setChecked(True)

        self.gridLayout_10.addWidget(self.checkbox_valor, 3, 0, 1, 1)

        self.checkbox_descripcion = QCheckBox(self.groupBox)
        self.checkbox_descripcion.setObjectName(u"checkbox_descripcion")
        self.checkbox_descripcion.setEnabled(False)
        self.checkbox_descripcion.setCheckable(True)
        self.checkbox_descripcion.setChecked(True)

        self.gridLayout_10.addWidget(self.checkbox_descripcion, 0, 0, 1, 1)

        self.checkbox_fecha = QCheckBox(self.groupBox)
        self.checkbox_fecha.setObjectName(u"checkbox_fecha")
        self.checkbox_fecha.setEnabled(True)
        self.checkbox_fecha.setCheckable(True)
        self.checkbox_fecha.setChecked(True)

        self.gridLayout_10.addWidget(self.checkbox_fecha, 1, 0, 1, 1)

        self.checkbox_hora = QCheckBox(self.groupBox)
        self.checkbox_hora.setObjectName(u"checkbox_hora")
        self.checkbox_hora.setEnabled(True)
        self.checkbox_hora.setCheckable(True)
        self.checkbox_hora.setChecked(True)

        self.gridLayout_10.addWidget(self.checkbox_hora, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_10.addWidget(self.label_5, 0, 1, 1, 1)

        self.spinbox_columnas = QSpinBox(self.groupBox)
        self.spinbox_columnas.setObjectName(u"spinbox_columnas")
        self.spinbox_columnas.setMinimumSize(QSize(0, 35))
        self.spinbox_columnas.setMinimum(0)
        self.spinbox_columnas.setMaximum(10)

        self.gridLayout_10.addWidget(self.spinbox_columnas, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_10.addWidget(self.label_6, 2, 1, 1, 1)

        self.spinbox_filas = QSpinBox(self.groupBox)
        self.spinbox_filas.setObjectName(u"spinbox_filas")
        self.spinbox_filas.setMinimumSize(QSize(0, 35))
        self.spinbox_filas.setMinimum(0)
        self.spinbox_filas.setMaximum(10)

        self.gridLayout_10.addWidget(self.spinbox_filas, 3, 1, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox, 3, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(458, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.agragar_nuevo_organizador_button = QPushButton(self.nuevo_organizador_page)
        self.agragar_nuevo_organizador_button.setObjectName(u"agragar_nuevo_organizador_button")
        sizePolicy1.setHeightForWidth(self.agragar_nuevo_organizador_button.sizePolicy().hasHeightForWidth())
        self.agragar_nuevo_organizador_button.setSizePolicy(sizePolicy1)
        self.agragar_nuevo_organizador_button.setMinimumSize(QSize(220, 55))
        self.agragar_nuevo_organizador_button.setMaximumSize(QSize(110, 55))
        self.agragar_nuevo_organizador_button.setFont(font2)
        self.agragar_nuevo_organizador_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.agragar_nuevo_organizador_button.setStyleSheet(u"QPushButton {\n"
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
        self.agragar_nuevo_organizador_button.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.agragar_nuevo_organizador_button)


        self.gridLayout_11.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)

        self.stackedWidget.addWidget(self.nuevo_organizador_page)
        self.Settings_page = QWidget()
        self.Settings_page.setObjectName(u"Settings_page")
        self.gridLayout_5 = QGridLayout(self.Settings_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(15)
        self.gridLayout_5.setVerticalSpacing(20)
        self.gridLayout_5.setContentsMargins(50, 50, 50, 50)
        self.verticalSpacer_7 = QSpacerItem(20, 407, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 10, -1, 10)
        self.about_us_button = QPushButton(self.Settings_page)
        self.about_us_button.setObjectName(u"about_us_button")
        sizePolicy1.setHeightForWidth(self.about_us_button.sizePolicy().hasHeightForWidth())
        self.about_us_button.setSizePolicy(sizePolicy1)
        self.about_us_button.setMinimumSize(QSize(200, 50))
        self.about_us_button.setMaximumSize(QSize(110, 40))
        self.about_us_button.setFont(font2)
        self.about_us_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_us_button.setStyleSheet(u"QPushButton {\n"
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
        self.about_us_button.setCheckable(True)

        self.verticalLayout_7.addWidget(self.about_us_button, 0, Qt.AlignLeft)

        self.support_button = QPushButton(self.Settings_page)
        self.support_button.setObjectName(u"support_button")
        sizePolicy1.setHeightForWidth(self.support_button.sizePolicy().hasHeightForWidth())
        self.support_button.setSizePolicy(sizePolicy1)
        self.support_button.setMinimumSize(QSize(200, 50))
        self.support_button.setMaximumSize(QSize(110, 40))
        self.support_button.setFont(font2)
        self.support_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.support_button.setStyleSheet(u"QPushButton {\n"
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
        self.support_button.setCheckable(True)

        self.verticalLayout_7.addWidget(self.support_button, 0, Qt.AlignLeft)


        self.gridLayout_5.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.label_8 = QLabel(self.Settings_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"font-size: 30px;")
        self.label_8.setLocale(QLocale(QLocale.Spanish, QLocale.Colombia))

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1, Qt.AlignLeft)

        self.stackedWidget.addWidget(self.Settings_page)
        self.suppot_page = QWidget()
        self.suppot_page.setObjectName(u"suppot_page")
        self.gridLayout_2 = QGridLayout(self.suppot_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(100, 100, 100, 100)
        self.plainTextEdit_support = QPlainTextEdit(self.suppot_page)
        self.plainTextEdit_support.setObjectName(u"plainTextEdit_support")
        self.plainTextEdit_support.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: rgba(103, 178, 98, 180); \n"
"    font-size: 17px;\n"
"    padding: 30px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    background-color: rgba(103, 178, 98, 150);\n"
"    font-size: 18px;\n"
"    border: 2px solid blue;\n"
"}")

        self.gridLayout_2.addWidget(self.plainTextEdit_support, 1, 0, 1, 1)

        self.list_apoyo = QListWidget(self.suppot_page)
        QListWidgetItem(self.list_apoyo)
        QListWidgetItem(self.list_apoyo)
        QListWidgetItem(self.list_apoyo)
        self.list_apoyo.setObjectName(u"list_apoyo")
        self.list_apoyo.setMinimumSize(QSize(0, 200))
        self.list_apoyo.setMaximumSize(QSize(16777215, 200))
        self.list_apoyo.setStyleSheet(u"QListWidget::item:hover {\n"
"    background-color: rgba(103, 178, 98, 150);\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: rgba(103, 178, 98, 200);\n"
"    font-size: 18px;\n"
"	color: black;\n"
"	border: none;\n"
"}\n"
"\n"
"QListWidget {\n"
"    background-color: rgba(103, 178, 98, 180); \n"
"    font-size: 17px;\n"
"    padding: 30px;\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.list_apoyo, 0, 0, 1, 1)

        self.enviar_buttton_apoyo = QPushButton(self.suppot_page)
        self.enviar_buttton_apoyo.setObjectName(u"enviar_buttton_apoyo")
        sizePolicy1.setHeightForWidth(self.enviar_buttton_apoyo.sizePolicy().hasHeightForWidth())
        self.enviar_buttton_apoyo.setSizePolicy(sizePolicy1)
        self.enviar_buttton_apoyo.setMinimumSize(QSize(200, 50))
        self.enviar_buttton_apoyo.setMaximumSize(QSize(110, 40))
        self.enviar_buttton_apoyo.setFont(font2)
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

        self.gridLayout_2.addWidget(self.enviar_buttton_apoyo, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.suppot_page)
        self.about_us_page = QWidget()
        self.about_us_page.setObjectName(u"about_us_page")
        self.gridLayout_3 = QGridLayout(self.about_us_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(50)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(50, 100, 50, 100)
        self.textBrowser = QTextBrowser(self.about_us_page)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy2)
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"    background-color: rgba(103, 178, 98, 180); \n"
"    font-size: 17px;\n"
"    padding: 30px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QTextBrowser:focus {\n"
"    background-color: rgba(103, 178, 98, 150);\n"
"    font-size: 18px;\n"
"    border: 2px solid blue; \n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.textBrowser, 0, 0, 3, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 129, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_gracias = QLabel(self.about_us_page)
        self.label_gracias.setObjectName(u"label_gracias")
        self.label_gracias.setMinimumSize(QSize(320, 90))
        self.label_gracias.setMaximumSize(QSize(320, 90))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(25)
        font3.setBold(True)
        self.label_gracias.setFont(font3)
        self.label_gracias.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_gracias)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_14 = QLabel(self.about_us_page)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setPixmap(QPixmap(u":/icons/Images/logo.png"))

        self.horizontalLayout.addWidget(self.label_14)

        self.label_pulse = QLabel(self.about_us_page)
        self.label_pulse.setObjectName(u"label_pulse")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_pulse.sizePolicy().hasHeightForWidth())
        self.label_pulse.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(20)
        font4.setBold(False)
        self.label_pulse.setFont(font4)

        self.horizontalLayout.addWidget(self.label_pulse)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.gridLayout_3.addLayout(self.verticalLayout_6, 1, 1, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 210, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.about_us_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_7.addWidget(self.main_menu)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1280, 22))
        self.menuArchivos = QMenu(self.menuBar)
        self.menuArchivos.setObjectName(u"menuArchivos")
        self.menuAcerca_de = QMenu(self.menuBar)
        self.menuAcerca_de.setObjectName(u"menuAcerca_de")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuArchivos.menuAction())
        self.menuBar.addAction(self.menuAcerca_de.menuAction())
        self.menuArchivos.addAction(self.actionExportar_organizador)
        self.menuArchivos.addAction(self.actionImportar_organizador)
        self.menuArchivos.addAction(self.actionSalir)
        self.menuAcerca_de.addAction(self.actionAcerca_De)
        self.menuAcerca_de.addAction(self.actionSoporte)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.new_1_button.toggled.connect(self.new_2_button.setChecked)
        self.new_2_button.toggled.connect(self.new_1_button.setChecked)
        self.singout_2.toggled.connect(MainWindow.close)
        self.singout_1.toggled.connect(MainWindow.close)
        self.singout_2.toggled.connect(self.singout_1.setChecked)
        self.singout_1.toggled.connect(self.singout_2.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)

        self.stackedWidget.setCurrentIndex(0)
        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExportar_organizador.setText(QCoreApplication.translate("MainWindow", u"Exportar organizador", None))
        self.actionImportar_organizador.setText(QCoreApplication.translate("MainWindow", u"Importar organizador", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionAcerca_De.setText(QCoreApplication.translate("MainWindow", u"Acerca De", None))
        self.actionSoporte.setText(QCoreApplication.translate("MainWindow", u"Soporte", None))
        self.label.setText("")
        self.dashboard_1.setText("")
        self.new_1_button.setText("")
        self.settings_1.setText("")
        self.singout_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"  My Organizer", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"  Organizadores", None))
        self.new_2_button.setText(QCoreApplication.translate("MainWindow", u"  Nuevo organizador", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"  Configuraci\u00f3n", None))
        self.singout_2.setText(QCoreApplication.translate("MainWindow", u"  Cerrar Sesi\u00f3n", None))
        self.menu.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Hora_label", None))
#if QT_CONFIG(accessibility)
        self.label_10.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tus organizadores", None))
        self.agregar_organizador_button.setText("")
        self.agregar_nueva_categoria_button.setText("")
        self.lineedit_nombretabla.setText("")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_seleccted), QCoreApplication.translate("MainWindow", u"Organizador seleccionado", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_total), QCoreApplication.translate("MainWindow", u"Todos los organizadores", None))
        ___qtreewidgetitem = self.treeWidget_organizadores.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Organizadores", None));

        __sortingEnabled = self.treeWidget_organizadores.isSortingEnabled()
        self.treeWidget_organizadores.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget_organizadores.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Familia", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Ni\u00f1os", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Antonella", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Pepito", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Pareja", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"Paseo", None));
        ___qtreewidgetitem7 = self.treeWidget_organizadores.topLevelItem(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"Trabajo", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"Transporte", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem7.child(1)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"Comida", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem7.child(2)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"Nuevo elemento", None));
        ___qtreewidgetitem11 = self.treeWidget_organizadores.topLevelItem(2)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"Viajes", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"Brasil", None));
        self.treeWidget_organizadores.setSortingEnabled(__sortingEnabled)

        self.eliminar_organizador_button.setText("")
        self.eliminar_tabla_button.setText("")
        self.nueva_columna_button.setText(QCoreApplication.translate("MainWindow", u"Nueva Columna", None))
        self.nueva_fila_button.setText(QCoreApplication.translate("MainWindow", u"Nueva Fila", None))
        self.edit_save_button.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
#if QT_CONFIG(accessibility)
        self.label_11.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Nuevo organizador", None))
        self.checkbox_organizador.setText(QCoreApplication.translate("MainWindow", u"Organizador", None))
        self.checkbox_suborganizador.setText(QCoreApplication.translate("MainWindow", u"Sub organizador", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Columnas por defecto", None))
        self.checkbox_valor.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.checkbox_descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.checkbox_fecha.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.checkbox_hora.setText(QCoreApplication.translate("MainWindow", u"Hora", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Culumnas Adicionales", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Filas Adicionales", None))
        self.agragar_nuevo_organizador_button.setText(QCoreApplication.translate("MainWindow", u"Agregar organizador", None))
        self.about_us_button.setText(QCoreApplication.translate("MainWindow", u"About us", None))
        self.support_button.setText(QCoreApplication.translate("MainWindow", u"Support", None))
#if QT_CONFIG(accessibility)
        self.label_8.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Configuraciones", None))

        __sortingEnabled1 = self.list_apoyo.isSortingEnabled()
        self.list_apoyo.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_apoyo.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Sugerencias", None));
        ___qlistwidgetitem1 = self.list_apoyo.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Comentarios", None));
        ___qlistwidgetitem2 = self.list_apoyo.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Otro", None));
        self.list_apoyo.setSortingEnabled(__sortingEnabled1)

        self.enviar_buttton_apoyo.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:17px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Desarrolladores:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Andres Felipe Martinez Guerra:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Universidad de Nari\u00f1o, estudiante de ingenier\u00eda de sistemas.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Sebastian David Ordo\u00f1ez Bola\u00f1oz:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family"
                        ":'Roboto','sans-serif'; font-size:12pt;\">Universidad de Nari\u00f1o, estudiante de ingenier\u00eda de sistemas.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Acerca de la app:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">es una app dise\u00f1ada para que organices tus gastos de manera ordenada, donde puedes guadar tus tablas de organizacion en excel o asi mismo exportarlas o importarlas para seguir trabajando en ellas</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">Contactos:<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">afmartinez23a@udenar.edu.co</span></p"
                        ">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','sans-serif'; font-size:12pt;\">sdordonez23a@udenar.edu.co</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto','sans-serif'; font-size:12pt;\"><br /></p></body></html>", None))
        self.label_gracias.setText(QCoreApplication.translate("MainWindow", u"Gracias por usar                       My Organizer :)", None))
        self.label_14.setText("")
        self.label_pulse.setText(QCoreApplication.translate("MainWindow", u"My Organizer", None))
        self.menuArchivos.setTitle(QCoreApplication.translate("MainWindow", u"Archivos", None))
        self.menuAcerca_de.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

