# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Laur\APP_UI\createPacient.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createPacientWindow(object):
    def setupUi(self, createPacientWindow):
        createPacientWindow.setObjectName("createPacientWindow")
        createPacientWindow.resize(1051, 771)
        createPacientWindow.setStyleSheet("background-color: rgb(211, 248, 244);")
        self.centralwidget = QtWidgets.QWidget(createPacientWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.backCrearePacientButton = QtWidgets.QPushButton(self.centralwidget)
        self.backCrearePacientButton.setMaximumSize(QtCore.QSize(41, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(133, 205, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 205, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 205, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 205, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 205, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 205, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 205, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 205, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 205, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.backCrearePacientButton.setPalette(palette)
        self.backCrearePacientButton.setStyleSheet("background-color: rgb(133, 205, 202);")
        self.backCrearePacientButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Laur\\APP_UI\\../Paciento/Paciento/resources/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backCrearePacientButton.setIcon(icon)
        self.backCrearePacientButton.setIconSize(QtCore.QSize(20, 20))
        self.backCrearePacientButton.setObjectName("backCrearePacientButton")
        self.verticalLayout_2.addWidget(self.backCrearePacientButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.numePacientLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numePacientLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numePacientLineEdit.setObjectName("numePacientLineEdit")
        self.horizontalLayout.addWidget(self.numePacientLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.prenumePacientLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.prenumePacientLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prenumePacientLineEdit.setObjectName("prenumePacientLineEdit")
        self.horizontalLayout_2.addWidget(self.prenumePacientLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.CNPPacientLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.CNPPacientLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CNPPacientLineEdit.setObjectName("CNPPacientLineEdit")
        self.horizontalLayout_3.addWidget(self.CNPPacientLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.telefonPacientLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.telefonPacientLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.telefonPacientLineEdit.setObjectName("telefonPacientLineEdit")
        self.horizontalLayout_4.addWidget(self.telefonPacientLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.emailPacientLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailPacientLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emailPacientLineEdit.setObjectName("emailPacientLineEdit")
        self.horizontalLayout_7.addWidget(self.emailPacientLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.dataNasterePacientTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dataNasterePacientTimeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dataNasterePacientTimeEdit.setObjectName("dataNasterePacientTimeEdit")
        self.horizontalLayout_8.addWidget(self.dataNasterePacientTimeEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.sexPacientcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.sexPacientcomboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sexPacientcomboBox.setObjectName("sexPacientcomboBox")
        self.sexPacientcomboBox.addItem("")
        self.sexPacientcomboBox.addItem("")
        self.horizontalLayout_13.addWidget(self.sexPacientcomboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.stradaPacientLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.stradaPacientLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stradaPacientLineEdit.setObjectName("stradaPacientLineEdit")
        self.horizontalLayout_9.addWidget(self.stradaPacientLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.numarPacientLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.numarPacientLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numarPacientLineEdit.setObjectName("numarPacientLineEdit")
        self.horizontalLayout_10.addWidget(self.numarPacientLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.localitatePacientLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.localitatePacientLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.localitatePacientLineEdit.setObjectName("localitatePacientLineEdit")
        self.horizontalLayout_11.addWidget(self.localitatePacientLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.judetPacientLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.judetPacientLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.judetPacientLineEdit.setObjectName("judetPacientLineEdit")
        self.horizontalLayout_12.addWidget(self.judetPacientLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.creazaPacientButton = QtWidgets.QPushButton(self.centralwidget)
        self.creazaPacientButton.setStyleSheet("background-color: rgb(195, 141, 158);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.creazaPacientButton.setObjectName("creazaPacientButton")
        self.verticalLayout_2.addWidget(self.creazaPacientButton)
        createPacientWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(createPacientWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 26))
        self.menubar.setObjectName("menubar")
        createPacientWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(createPacientWindow)
        self.statusbar.setObjectName("statusbar")
        createPacientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(createPacientWindow)
        QtCore.QMetaObject.connectSlotsByName(createPacientWindow)

    def retranslateUi(self, createPacientWindow):
        _translate = QtCore.QCoreApplication.translate
        createPacientWindow.setWindowTitle(_translate("createPacientWindow", "MainWindow"))
        self.label.setText(_translate("createPacientWindow", "Nume:"))
        self.label_2.setText(_translate("createPacientWindow", "Prenume:"))
        self.label_3.setText(_translate("createPacientWindow", "CNP:"))
        self.label_4.setText(_translate("createPacientWindow", "Telefon:"))
        self.label_7.setText(_translate("createPacientWindow", "Email:"))
        self.label_8.setText(_translate("createPacientWindow", "DataNasterii:"))
        self.label_13.setText(_translate("createPacientWindow", "Sex:"))
        self.sexPacientcomboBox.setItemText(0, _translate("createPacientWindow", "Male"))
        self.sexPacientcomboBox.setItemText(1, _translate("createPacientWindow", "Female"))
        self.groupBox.setTitle(_translate("createPacientWindow", "Adresa"))
        self.label_9.setText(_translate("createPacientWindow", "Strada:"))
        self.label_10.setText(_translate("createPacientWindow", "Numar:"))
        self.label_11.setText(_translate("createPacientWindow", "Localitate:"))
        self.label_12.setText(_translate("createPacientWindow", "Judet:"))
        self.creazaPacientButton.setText(_translate("createPacientWindow", "Creaza pacient"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createPacientWindow = QtWidgets.QMainWindow()
    ui = Ui_createPacientWindow()
    ui.setupUi(createPacientWindow)
    createPacientWindow.show()
    sys.exit(app.exec_())