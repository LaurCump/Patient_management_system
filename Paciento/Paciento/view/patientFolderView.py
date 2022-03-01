# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Laur\APP_UI\patientFolder.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_patientFolderWindow(object):
    def setupUi(self, patientFolderWindow):
        patientFolderWindow.setObjectName("patientFolderWindow")
        patientFolderWindow.resize(1097, 866)
        patientFolderWindow.setStyleSheet("background-color: rgb(211, 248, 244);")
        self.centralwidget = QtWidgets.QWidget(patientFolderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.backPatientFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.backPatientFolderButton.setMaximumSize(QtCore.QSize(41, 31))
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
        self.backPatientFolderButton.setPalette(palette)
        self.backPatientFolderButton.setStyleSheet("background-color: rgb(133, 205, 202);")
        self.backPatientFolderButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Laur\\APP_UI\\../Paciento/Paciento/resources/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backPatientFolderButton.setIcon(icon)
        self.backPatientFolderButton.setIconSize(QtCore.QSize(20, 20))
        self.backPatientFolderButton.setObjectName("backPatientFolderButton")
        self.verticalLayout_3.addWidget(self.backPatientFolderButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.numePacientLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.numePacientLineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numePacientLineEdit_2.setObjectName("numePacientLineEdit_2")
        self.horizontalLayout_6.addWidget(self.numePacientLineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_20.addWidget(self.label_20)
        self.prenumePacientLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.prenumePacientLineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.prenumePacientLineEdit_2.setObjectName("prenumePacientLineEdit_2")
        self.horizontalLayout_20.addWidget(self.prenumePacientLineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.CNPPacientLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.CNPPacientLineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CNPPacientLineEdit_2.setObjectName("CNPPacientLineEdit_2")
        self.horizontalLayout_5.addWidget(self.CNPPacientLineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_21.addWidget(self.label_21)
        self.telefonPacientLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.telefonPacientLineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.telefonPacientLineEdit_2.setObjectName("telefonPacientLineEdit_2")
        self.horizontalLayout_21.addWidget(self.telefonPacientLineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_19.addWidget(self.label_19)
        self.emailPacientLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.emailPacientLineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emailPacientLineEdit_2.setObjectName("emailPacientLineEdit_2")
        self.horizontalLayout_19.addWidget(self.emailPacientLineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_22.addWidget(self.label_22)
        self.dataNasterePacientTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dataNasterePacientTimeEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dataNasterePacientTimeEdit_2.setObjectName("dataNasterePacientTimeEdit_2")
        self.horizontalLayout_22.addWidget(self.dataNasterePacientTimeEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_14.addWidget(self.label_14)
        self.sexPacientcomboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.sexPacientcomboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sexPacientcomboBox_2.setObjectName("sexPacientcomboBox_2")
        self.sexPacientcomboBox_2.addItem("")
        self.sexPacientcomboBox_2.addItem("")
        self.horizontalLayout_14.addWidget(self.sexPacientcomboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_23)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_15.addWidget(self.label_15)
        self.stradaPacientLineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.stradaPacientLineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stradaPacientLineEdit_2.setObjectName("stradaPacientLineEdit_2")
        self.horizontalLayout_15.addWidget(self.stradaPacientLineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.numarPacientLineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.numarPacientLineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numarPacientLineEdit_2.setObjectName("numarPacientLineEdit_2")
        self.horizontalLayout_16.addWidget(self.numarPacientLineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_17.addWidget(self.label_17)
        self.localitatePacientLineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.localitatePacientLineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.localitatePacientLineEdit_2.setObjectName("localitatePacientLineEdit_2")
        self.horizontalLayout_17.addWidget(self.localitatePacientLineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_18.addWidget(self.label_18)
        self.judetPacientLineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.judetPacientLineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.judetPacientLineEdit_2.setObjectName("judetPacientLineEdit_2")
        self.horizontalLayout_18.addWidget(self.judetPacientLineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.stergePacientButton = QtWidgets.QPushButton(self.centralwidget)
        self.stergePacientButton.setMaximumSize(QtCore.QSize(151, 59))
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
        self.stergePacientButton.setPalette(palette)
        self.stergePacientButton.setStyleSheet("background-color: rgb(133, 205, 202);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\Laur\\APP_UI\\../Paciento/Paciento/resources/bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stergePacientButton.setIcon(icon1)
        self.stergePacientButton.setIconSize(QtCore.QSize(30, 30))
        self.stergePacientButton.setObjectName("stergePacientButton")
        self.verticalLayout_3.addWidget(self.stergePacientButton)
        patientFolderWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(patientFolderWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 26))
        self.menubar.setObjectName("menubar")
        patientFolderWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(patientFolderWindow)
        self.statusbar.setObjectName("statusbar")
        patientFolderWindow.setStatusBar(self.statusbar)

        self.retranslateUi(patientFolderWindow)
        QtCore.QMetaObject.connectSlotsByName(patientFolderWindow)

    def retranslateUi(self, patientFolderWindow):
        _translate = QtCore.QCoreApplication.translate
        patientFolderWindow.setWindowTitle(_translate("patientFolderWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("patientFolderWindow", "Informatii"))
        self.label_6.setText(_translate("patientFolderWindow", "Nume:"))
        self.label_20.setText(_translate("patientFolderWindow", "Prenume:"))
        self.label_5.setText(_translate("patientFolderWindow", "CNP:"))
        self.label_21.setText(_translate("patientFolderWindow", "Telefon:"))
        self.label_19.setText(_translate("patientFolderWindow", "Email:"))
        self.label_22.setText(_translate("patientFolderWindow", "DataNasterii:"))
        self.label_14.setText(_translate("patientFolderWindow", "Sex:"))
        self.sexPacientcomboBox_2.setItemText(0, _translate("patientFolderWindow", "Male"))
        self.sexPacientcomboBox_2.setItemText(1, _translate("patientFolderWindow", "Female"))
        self.groupBox.setTitle(_translate("patientFolderWindow", "Adresa"))
        self.label_15.setText(_translate("patientFolderWindow", "Strada:"))
        self.label_16.setText(_translate("patientFolderWindow", "Numar:"))
        self.label_17.setText(_translate("patientFolderWindow", "Localitate:"))
        self.label_18.setText(_translate("patientFolderWindow", "Judet:"))
        self.stergePacientButton.setText(_translate("patientFolderWindow", "Sterge pacient"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    patientFolderWindow = QtWidgets.QMainWindow()
    ui = Ui_patientFolderWindow()
    ui.setupUi(patientFolderWindow)
    patientFolderWindow.show()
    sys.exit(app.exec_())
