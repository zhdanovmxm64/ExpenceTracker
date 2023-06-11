# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rs

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.954545, y2:1, stop:0 rgba(77, 170, 70, 255), stop:1 rgba(255, 255, 255, 255))\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.horizontalLayout_7 = QHBoxLayout(self.balance_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.balance_frame_2 = QFrame(self.balance_frame)
        self.balance_frame_2.setObjectName(u"balance_frame_2")
        self.balance_frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.label_current_balance = QLabel(self.balance_frame_2)
        self.label_current_balance.setObjectName(u"label_current_balance")
        self.label_current_balance.setStyleSheet(u"color: #00859d;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_current_balance)

        self.label_balance = QLabel(self.balance_frame_2)
        self.label_balance.setObjectName(u"label_balance")
        self.label_balance.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_balance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_up_arrow = QLabel(self.balance_frame_2)
        self.icon_up_arrow.setObjectName(u"icon_up_arrow")
        self.icon_up_arrow.setMaximumSize(QSize(24, 16777215))
        self.icon_up_arrow.setStyleSheet(u"\n"
"background-color: none;\n"
"border: none;\n"
"font-weught: bold;\n"
"padding-top: 10px;")
        self.icon_up_arrow.setPixmap(QPixmap(u":/icon/icon/call_made_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout.addWidget(self.icon_up_arrow)

        self.label_income = QLabel(self.balance_frame_2)
        self.label_income.setObjectName(u"label_income")
        self.label_income.setStyleSheet(u"\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.label_income)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.income_balance = QLabel(self.balance_frame_2)
        self.income_balance.setObjectName(u"income_balance")
        self.income_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.income_balance)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon_down_balance = QLabel(self.balance_frame_2)
        self.icon_down_balance.setObjectName(u"icon_down_balance")
        self.icon_down_balance.setMaximumSize(QSize(24, 16777215))
        self.icon_down_balance.setStyleSheet(u"\n"
"background-color: none;\n"
"border: none;\n"
"font-weught: bold;\n"
"padding-top: 10px;")
        self.icon_down_balance.setPixmap(QPixmap(u":/icon/icon/call_received_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_2.addWidget(self.icon_down_balance)

        self.label_outcome = QLabel(self.balance_frame_2)
        self.label_outcome.setObjectName(u"label_outcome")
        self.label_outcome.setStyleSheet(u"\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.label_outcome)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.outcome_balance = QLabel(self.balance_frame_2)
        self.outcome_balance.setObjectName(u"outcome_balance")
        self.outcome_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.outcome_balance)


        self.horizontalLayout_7.addWidget(self.balance_frame_2)

        self.categories_frame = QFrame(self.balance_frame)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.le_expence_catigories = QLabel(self.categories_frame)
        self.le_expence_catigories.setObjectName(u"le_expence_catigories")
        self.le_expence_catigories.setStyleSheet(u"color: #00859d;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.le_expence_catigories)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_groceries = QLabel(self.categories_frame)
        self.icon_groceries.setObjectName(u"icon_groceries")
        self.icon_groceries.setMaximumSize(QSize(24, 16777215))
        self.icon_groceries.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_groceries.setPixmap(QPixmap(u":/icon/icon/shopping_cart_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_3.addWidget(self.icon_groceries)

        self.label_groceries = QLabel(self.categories_frame)
        self.label_groceries.setObjectName(u"label_groceries")
        self.label_groceries.setStyleSheet(u"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.label_groceries)

        self.balance_groceries = QLabel(self.categories_frame)
        self.balance_groceries.setObjectName(u"balance_groceries")
        self.balance_groceries.setStyleSheet(u"color: #00859d;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.balance_groceries)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_entertaiment = QLabel(self.categories_frame)
        self.icon_entertaiment.setObjectName(u"icon_entertaiment")
        self.icon_entertaiment.setMaximumSize(QSize(24, 16777215))
        self.icon_entertaiment.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_entertaiment.setPixmap(QPixmap(u":/icon/icon/stadia_controller_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_4.addWidget(self.icon_entertaiment)

        self.label_entertaiment = QLabel(self.categories_frame)
        self.label_entertaiment.setObjectName(u"label_entertaiment")
        self.label_entertaiment.setStyleSheet(u"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;")

        self.horizontalLayout_4.addWidget(self.label_entertaiment)

        self.balance_entertaiment = QLabel(self.categories_frame)
        self.balance_entertaiment.setObjectName(u"balance_entertaiment")
        self.balance_entertaiment.setStyleSheet(u"color: #00859d;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.balance_entertaiment)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icon_auto = QLabel(self.categories_frame)
        self.icon_auto.setObjectName(u"icon_auto")
        self.icon_auto.setMaximumSize(QSize(24, 16777215))
        self.icon_auto.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_auto.setPixmap(QPixmap(u":/icon/icon/directions_car_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_5.addWidget(self.icon_auto)

        self.label_auto = QLabel(self.categories_frame)
        self.label_auto.setObjectName(u"label_auto")
        self.label_auto.setStyleSheet(u"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;")

        self.horizontalLayout_5.addWidget(self.label_auto)

        self.balance_auto = QLabel(self.categories_frame)
        self.balance_auto.setObjectName(u"balance_auto")
        self.balance_auto.setStyleSheet(u"color: #00859d;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.balance_auto)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.icon_other = QLabel(self.categories_frame)
        self.icon_other.setObjectName(u"icon_other")
        self.icon_other.setMaximumSize(QSize(24, 16777215))
        self.icon_other.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_other.setPixmap(QPixmap(u":/icon/icon/other_admission_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_6.addWidget(self.icon_other)

        self.label_other = QLabel(self.categories_frame)
        self.label_other.setObjectName(u"label_other")
        self.label_other.setStyleSheet(u"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;")

        self.horizontalLayout_6.addWidget(self.label_other)

        self.balance_other = QLabel(self.categories_frame)
        self.balance_other.setObjectName(u"balance_other")
        self.balance_other.setStyleSheet(u"color: #00859d;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.balance_other)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addWidget(self.categories_frame)


        self.verticalLayout_3.addWidget(self.balance_frame)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_new_transaction = QPushButton(self.centralwidget)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setStyleSheet(u"QPushButton {\n"
"	alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.954545, y2:1, stop:0 rgba(77, 170, 70, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"}\n"
"QPushButton:pressed {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon/create_new_folder_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_new_transaction)

        self.btn_edit_transaction = QPushButton(self.centralwidget)
        self.btn_edit_transaction.setObjectName(u"btn_edit_transaction")
        self.btn_edit_transaction.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.954545, y2:1, stop:0 rgba(77, 170, 70, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"}\n"
"QPushButton:pressed {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/edit_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_transaction.setIcon(icon1)
        self.btn_edit_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_edit_transaction)

        self.btn_delete_transaction = QPushButton(self.centralwidget)
        self.btn_delete_transaction.setObjectName(u"btn_delete_transaction")
        self.btn_delete_transaction.setStyleSheet(u"QPushButton {\n"
"border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.954545, y2:1, stop:0 rgba(77, 170, 70, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"}\n"
"QPushButton:pressed {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/delete_forever_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_transaction.setIcon(icon2)
        self.btn_delete_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.btn_delete_transaction)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"QTableView:section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableView:item {\n"
"border-stile: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"QTableView:item:selected {\n"
"border: none;\n"
"color: rgba(255, 255, 255,);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Expence Tacker", None))
        self.label_current_balance.setText(QCoreApplication.translate("MainWindow", u"Current Balance", None))
        self.label_balance.setText(QCoreApplication.translate("MainWindow", u"1200$", None))
        self.icon_up_arrow.setText("")
        self.label_income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.income_balance.setText(QCoreApplication.translate("MainWindow", u"1200$", None))
        self.icon_down_balance.setText("")
        self.label_outcome.setText(QCoreApplication.translate("MainWindow", u"Outcome", None))
        self.outcome_balance.setText(QCoreApplication.translate("MainWindow", u"1200$", None))
        self.le_expence_catigories.setText(QCoreApplication.translate("MainWindow", u"Expence catigories", None))
        self.icon_groceries.setText("")
        self.label_groceries.setText(QCoreApplication.translate("MainWindow", u"Groceries", None))
        self.balance_groceries.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_entertaiment.setText("")
        self.label_entertaiment.setText(QCoreApplication.translate("MainWindow", u"Entertaiment", None))
        self.balance_entertaiment.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_auto.setText("")
        self.label_auto.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.balance_auto.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_other.setText("")
        self.label_other.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.balance_other.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("MainWindow", u"New transaction", None))
        self.btn_edit_transaction.setText(QCoreApplication.translate("MainWindow", u"Edit transaction", None))
        self.btn_delete_transaction.setText(QCoreApplication.translate("MainWindow", u"Delete transaction", None))
    # retranslateUi

