# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Laur\APP_UI\createAccount.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createAccountWindow(object):
    def setupUi(self, createAccountWindow):
        createAccountWindow.setObjectName("createAccountWindow")
        createAccountWindow.resize(934, 732)
        createAccountWindow.setStyleSheet("background-color: rgb(211, 248, 244);")
        self.centralwidget = QtWidgets.QWidget(createAccountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.numeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numeLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numeLineEdit.setObjectName("numeLineEdit")
        self.horizontalLayout.addWidget(self.numeLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.prenumeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.prenumeLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prenumeLineEdit.setObjectName("prenumeLineEdit")
        self.horizontalLayout_2.addWidget(self.prenumeLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.CNPLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.CNPLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CNPLineEdit.setObjectName("CNPLineEdit")
        self.horizontalLayout_3.addWidget(self.CNPLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.telefonLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.telefonLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.telefonLineEdit.setObjectName("telefonLineEdit")
        self.horizontalLayout_4.addWidget(self.telefonLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.horizontalLayout_5.addWidget(self.emailLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_6.addWidget(self.dateTimeEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.nrCabinetLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nrCabinetLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nrCabinetLineEdit.setObjectName("nrCabinetLineEdit")
        self.horizontalLayout_7.addWidget(self.nrCabinetLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.parolaLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.parolaLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.parolaLineEdit.setObjectName("parolaLineEdit")
        self.horizontalLayout_8.addWidget(self.parolaLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.parolaConfLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.parolaConfLineEdit.setMinimumSize(QtCore.QSize(500, 0))
        self.parolaConfLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.parolaConfLineEdit.setObjectName("parolaConfLineEdit")
        self.horizontalLayout_9.addWidget(self.parolaConfLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setStyleSheet("background-color: rgb(195, 141, 158);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.createButton.setObjectName("createButton")
        self.verticalLayout.addWidget(self.createButton)
        createAccountWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(createAccountWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 26))
        self.menubar.setObjectName("menubar")
        createAccountWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(createAccountWindow)
        self.statusbar.setObjectName("statusbar")
        createAccountWindow.setStatusBar(self.statusbar)

        self.retranslateUi(createAccountWindow)
        QtCore.QMetaObject.connectSlotsByName(createAccountWindow)

    def retranslateUi(self, createAccountWindow):
        _translate = QtCore.QCoreApplication.translate
        createAccountWindow.setWindowTitle(_translate("createAccountWindow", "MainWindow"))
        self.label.setText(_translate("createAccountWindow", "Nume:"))
        self.label_2.setText(_translate("createAccountWindow", "Prenume:"))
        self.label_3.setText(_translate("createAccountWindow", "CNP:"))
        self.label_4.setText(_translate("createAccountWindow", "Telefon:"))
        self.label_5.setText(_translate("createAccountWindow", "Email:"))
        self.label_6.setText(_translate("createAccountWindow", "DataNasterii:"))
        self.label_7.setText(_translate("createAccountWindow", "NrCabinet:"))
        self.label_8.setText(_translate("createAccountWindow", "Parola:"))
        self.label_9.setText(_translate("createAccountWindow", "Confirma parola:"))
        self.createButton.setText(_translate("createAccountWindow", "Creaza cont"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createAccountWindow = QtWidgets.QMainWindow()
    ui = Ui_createAccountWindow()
    ui.setupUi(createAccountWindow)
    createAccountWindow.show()
    sys.exit(app.exec_())
