# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import rec-rcpush_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(456, 439)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.954545, y2:1, stop:0 rgba(77, 170, 70, 255), stop:1 rgba(255, 255, 255, 255))\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_new_transaction = QLabel(self.frame)
        self.lbl_new_transaction.setObjectName(u"lbl_new_transaction")
        self.lbl_new_transaction.setStyleSheet(u"color: #00859d;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: rgba(255, 255, 255, 100);\n"
"border: none;\n"
"")
        self.lbl_new_transaction.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_new_transaction)

        self.cb_category = QComboBox(self.frame)
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.addItem("")
        self.cb_category.setObjectName(u"cb_category")
        self.cb_category.setStyleSheet(u"QComboBox{\n"
"font-size: 16pt;\n"
"\n"
"background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"QComboBox:item {\n"
"color:white;\n"
"background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.cb_category)

        self.data = QDateEdit(self.frame)
        self.data.setObjectName(u"data")
        self.data.setStyleSheet(u"padding-left: 10px;\n"
"font-size: 16pt;\n"
"background-color: rgba(255, 255, 255, 100);\n"
"border: none;")
        self.data.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.data.setDate(QDate(2023, 1, 1))

        self.verticalLayout.addWidget(self.data)

        self.le_description = QLineEdit(self.frame)
        self.le_description.setObjectName(u"le_description")
        self.le_description.setStyleSheet(u"padding-left: 10px;\n"
"font-size: 16pt;\n"
"background-color: rgba(255, 255, 255, 100);\n"
"border: none;")

        self.verticalLayout.addWidget(self.le_description)

        self.le_balance = QLineEdit(self.frame)
        self.le_balance.setObjectName(u"le_balance")
        self.le_balance.setStyleSheet(u"padding-left: 10px;\n"
"font-size: 16pt;\n"
"background-color: rgba(255, 255, 255, 100);\n"
"border: none;")

        self.verticalLayout.addWidget(self.le_balance)

        self.cb_income = QComboBox(self.frame)
        self.cb_income.addItem("")
        self.cb_income.addItem("")
        self.cb_income.setObjectName(u"cb_income")
        self.cb_income.setStyleSheet(u"QComboBox{\n"
"font-size: 16pt;\n"
"\n"
"background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"QComboBox:item {\n"
"color:white;\n"
"background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.cb_income)

        self.btn_new_transaction = QPushButton(self.frame)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/icon/done_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_new_transaction)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.cb_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_transaction.setText(QCoreApplication.translate("Dialog", u"New transaction", None))
        self.cb_category.setItemText(0, QCoreApplication.translate("Dialog", u"Groceries", None))
        self.cb_category.setItemText(1, QCoreApplication.translate("Dialog", u"Entertaiment", None))
        self.cb_category.setItemText(2, QCoreApplication.translate("Dialog", u"Auto", None))
        self.cb_category.setItemText(3, QCoreApplication.translate("Dialog", u"Other", None))
        self.cb_category.setItemText(4, QCoreApplication.translate("Dialog", u"Work", None))

        self.cb_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category", None))
        self.le_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.le_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.cb_income.setItemText(0, QCoreApplication.translate("Dialog", u"Income", None))
        self.cb_income.setItemText(1, QCoreApplication.translate("Dialog", u"Outcome", None))

        self.btn_new_transaction.setText(QCoreApplication.translate("Dialog", u"Save new transaction", None))
    # retranslateUi

