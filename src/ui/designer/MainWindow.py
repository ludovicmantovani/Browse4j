# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QCommandLinkButton,
    QDockWidget,
    QGraphicsView,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QStatusBar,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.actionShowBDDDock = QAction(MainWindow)
        self.actionShowBDDDock.setObjectName("actionShowBDDDock")
        self.actionShowBDDDock.setCheckable(True)
        self.actionShowBDDDock.setChecked(True)
        self.actionShowBDDDock.setMenuRole(QAction.MenuRole.NoRole)
        self.actionShowCypherDock = QAction(MainWindow)
        self.actionShowCypherDock.setObjectName("actionShowCypherDock")
        self.actionShowCypherDock.setCheckable(True)
        self.actionShowCypherDock.setChecked(True)
        self.actionShowCypherDock.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 9)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")

        self.horizontalLayout_2.addWidget(self.graphicsView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 33))
        self.menuFiles = QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuEdition = QMenu(self.menubar)
        self.menuEdition.setObjectName("menuEdition")
        self.menuAffichage = QMenu(self.menubar)
        self.menuAffichage.setObjectName("menuAffichage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockBDD = QDockWidget(MainWindow)
        self.dockBDD.setObjectName("dockBDD")
        self.dockBDD.setAllowedAreas(
            Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea
        )
        self.dockBDDContents = QWidget()
        self.dockBDDContents.setObjectName("dockBDDContents")
        self.verticalLayout_4 = QVBoxLayout(self.dockBDDContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, -1)
        self.listWidget = QListWidget(self.dockBDDContents)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)

        self.verticalLayout_4.addWidget(self.listWidget)

        self.dockBDD.setWidget(self.dockBDDContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockBDD)
        self.dockCypher = QDockWidget(MainWindow)
        self.dockCypher.setObjectName("dockCypher")
        self.dockCypher.setAllowedAreas(
            Qt.DockWidgetArea.BottomDockWidgetArea | Qt.DockWidgetArea.TopDockWidgetArea
        )
        self.dockCypherContents = QWidget()
        self.dockCypherContents.setObjectName("dockCypherContents")
        self.horizontalLayout = QHBoxLayout(self.dockCypherContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QTabWidget(self.dockCypherContents)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName("textEdit")

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.commandLinkButton = QCommandLinkButton(self.tab)
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.horizontalLayout_3.addWidget(
            self.commandLinkButton, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.label.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByKeyboard
            | Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextBrowserInteraction
            | Qt.TextInteractionFlag.TextSelectableByKeyboard
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )

        self.horizontalLayout_4.addWidget(self.label)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.dockCypher.setWidget(self.dockCypherContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.dockCypher)

        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuEdition.menuAction())
        self.menubar.addAction(self.menuAffichage.menuAction())
        self.menuAffichage.addAction(self.actionShowBDDDock)
        self.menuAffichage.addAction(self.actionShowCypherDock)
        self.menuAffichage.addSeparator()

        self.retranslateUi(MainWindow)
        self.actionShowBDDDock.toggled.connect(self.dockBDD.setVisible)
        self.dockBDD.visibilityChanged.connect(self.actionShowBDDDock.setChecked)
        self.dockCypher.visibilityChanged.connect(self.actionShowCypherDock.setChecked)
        self.actionShowCypherDock.toggled.connect(self.dockCypher.setVisible)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Browse4j", None))
        self.actionShowBDDDock.setText(
            QCoreApplication.translate("MainWindow", "Base de donn\u00e9es", None)
        )
        self.actionShowCypherDock.setText(QCoreApplication.translate("MainWindow", "Cypher", None))
        self.menuFiles.setTitle(QCoreApplication.translate("MainWindow", "Fichier", None))
        self.menuEdition.setTitle(QCoreApplication.translate("MainWindow", "Edition", None))
        self.menuAffichage.setTitle(QCoreApplication.translate("MainWindow", "Affichage", None))
        self.dockBDD.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Base de donn\u00e9es", None)
        )

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", "Bdd1", None))
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", "Bdd2", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.dockCypher.setWindowTitle(QCoreApplication.translate("MainWindow", "Cypher", None))
        self.commandLinkButton.setText(
            QCoreApplication.translate("MainWindow", "CommandLinkButton", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "Requ\u00eate", None),
        )
        self.label.setText(QCoreApplication.translate("MainWindow", "TextLabel", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Erreur", None),
        )

    # retranslateUi
