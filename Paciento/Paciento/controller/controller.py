from view.loginView import Ui_LoginWindow
from view.createAccountView import Ui_createAccountWindow
from view.mainPageView import  Ui_mainPageWindow
from view.createPacientView import  Ui_createPacientWindow
from view.patientFolderView import Ui_patientFolderWindow
from view.patientHistoryView import Ui_patientHistoryWindow
from view.createDiagnosticView import Ui_createDiagnosticWindow
from view.createPrescriptionView import Ui_createPrescriptionWindow
from view.createAppointmentView import Ui_createAppointmentWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox, QListWidgetItem
from model import model
from datetime import datetime
import sys


from view.mainPageView import Ui_mainPageWindow


class Controller:
    def __init__(self):
        self.emailMedicLogged = None
        self.passwordMedicLogged = None
        self.app = QApplication(sys.argv)

        self.login_window = Ui_LoginWindow()
        self.createAccount_window = Ui_createAccountWindow()
        self.mainPage_window = Ui_mainPageWindow()
        self.createPacient_window = Ui_createPacientWindow()
        self.patientFolder_window = Ui_patientFolderWindow()
        self.patientHistory_window = Ui_patientHistoryWindow()
        self.createDiagnostic_window = Ui_createDiagnosticWindow()
        self.createPrescription_window = Ui_createPrescriptionWindow()
        self.createAppointment_window = Ui_createAppointmentWindow()
        self.window = QMainWindow()
        self.load_loginWindow()


    def runApp(self):
        self.window.show()
        sys.exit(self.app.exec_())


    # loads the loginWindow page 
    def load_loginWindow(self):
        self.login_window.setupUi(self.window)
        self.login_window.passwordLineEdit.setEchoMode(QLineEdit.Password)

        # signal and slots
        self.login_window.loginButton.clicked.connect(self.loginHandler)
        self.login_window.accountNewButton.clicked.connect(self.load_createAccountWindow)
        

    # loads the createAccountWindow page 
    def load_createAccountWindow(self):
        self.createAccount_window.setupUi(self.window)
        self.createAccount_window.parolaLineEdit.setEchoMode(QLineEdit.Password)
        self.createAccount_window.parolaConfLineEdit.setEchoMode(QLineEdit.Password)

        # signal and slots
        self.createAccount_window.createButton.clicked.connect(self.createAccountHandler)   


    # loads the mainPageWindow page 
    def load_mainPageWindow(self):
        self.mainPage_window.setupUi(self.window)
        self.mainPage_window.numarPacientiLabel.setText("Numar total pacienti: " + str(model.numberPatients(self.emailMedicLogged, self.passwordMedicLogged)) + "      " + "Pacientul cel mai in varsta este: " + str(model.getOLderPatient(self.emailMedicLogged, self.passwordMedicLogged)))
        self.mainPage_window.listaPacientiWidget.clear()
        patientsList = model.getListPatients(self.emailMedicLogged, self.passwordMedicLogged)
        for pacient in patientsList:
            QListWidgetItem(pacient[0], self.mainPage_window.listaPacientiWidget)

        # signal and slots
        self.mainPage_window.adaugaPacientButton.clicked.connect(self.load_createPacientWindow)
        self.mainPage_window.dosarPacientButton.clicked.connect(self.viewPatientFolderHandler)
        self.mainPage_window.istoricPacientButton.clicked.connect(self.viewPatientHistoryHandler)
        self.mainPage_window.programariButton.clicked.connect(self.load_createAppointmentWindow)
        self.mainPage_window.searchButton.clicked.connect(self.searchPatientHandler)

    
    # loads the createPacientWindow page 
    def load_createPacientWindow(self):
        self.createPacient_window.setupUi(self.window)

        # signal and slots
        self.createPacient_window.backCrearePacientButton.clicked.connect(self.load_mainPageWindow)
        self.createPacient_window.creazaPacientButton.clicked.connect(self.createPatientHandler)


    # loads the patientFolderWindow page 
    def load_patientFolderWindow(self, info):
        self.patientFolder_window.setupUi(self.window)

        self.patientFolder_window.numePacientLineEdit_2.setText(info[2])
        self.patientFolder_window.prenumePacientLineEdit_2.setText(info[3])
        self.patientFolder_window.CNPPacientLineEdit_2.setText(info[4])
        self.patientFolder_window.telefonPacientLineEdit_2.setText(info[5])
        self.patientFolder_window.emailPacientLineEdit_2.setText(info[6])
        self.patientFolder_window.dataNasterePacientTimeEdit_2.setDateTime(info[7])
        self.patientFolder_window.stradaPacientLineEdit_2.setText(info[8])
        self.patientFolder_window.numarPacientLineEdit_2.setText(info[9])
        self.patientFolder_window.localitatePacientLineEdit_2.setText(info[10])
        self.patientFolder_window.judetPacientLineEdit_2.setText(info[11])
        if (info[12] == "M"):
            self.patientFolder_window.sexPacientcomboBox_2.setCurrentText("Male")
        else:
            self.patientFolder_window.sexPacientcomboBox_2.setCurrentText("Female")

        # signal and slots
        self.patientFolder_window.backPatientFolderButton.clicked.connect(self.load_mainPageWindow)
        self.patientFolder_window.stergePacientButton.clicked.connect(self.deletePatientHandler)

     
    # loads the patientHistoryWindow page 
    def load_patientHistoryWindow(self, info, cnp_pacient):  
        self.patientHistory_window.setupUi(self.window)
        self.patientHistory_window.listaDiagnosticeWidget.clear()
        for diagnostic in info:
            QListWidgetItem(diagnostic[0], self.patientHistory_window.listaDiagnosticeWidget)

        # signal and slots
        self.patientHistory_window.backPatientHistoryButton.clicked.connect(self.load_mainPageWindow)
        self.patientHistory_window.adaugaDiagnosticButton.clicked.connect(lambda : self.load_createDiagnosticWindow(info, cnp_pacient))
        self.patientHistory_window.stergeDiagnosticButton.clicked.connect(lambda : self.deleteDiagnosticHandler(cnp_pacient))
        self.patientHistory_window.vizualizareRetetaButton.clicked.connect(lambda : self.load_createPrescriptionWindow(cnp_pacient))


    # loads the createDiagnosticWindow page
    def load_createDiagnosticWindow(self, info, cnp_pacient):
        self.createDiagnostic_window.setupUi(self.window)

        # signals and slots
        self.createDiagnostic_window.backCreateDagnosticButton.clicked.connect(lambda : self.load_patientHistoryWindow(info, cnp_pacient))
        self.createDiagnostic_window.adaugaRetetaButton.clicked.connect(lambda : self.addDiagnostic(cnp_pacient))


    # loads the createPrescriptionWindow page when cerating a diagnostic
    def load_createPrescriptionWindowDiag(self, idPacientDiagnostic, cnp_pacient):
        self.createPrescription_window.setupUi(self.window)
        all_meds = model.getAllMeds()

        self.createPrescription_window.numeMedicamentComboBox.clear()
        for med in all_meds:
            self.createPrescription_window.numeMedicamentComboBox.addItem(med[0])

        # sigals and slots
        self.createPrescription_window.adugaMedicamentButton.clicked.connect(lambda: self.addMedHandler(cnp_pacient, idPacientDiagnostic))
        self.createPrescription_window.editareMedicamentButton.clicked.connect(lambda : self.updateMedHandler(cnp_pacient, idPacientDiagnostic))
        self.createPrescription_window.stergereMedicamentButton.clicked.connect(lambda : self.deleteMedHandler(cnp_pacient, idPacientDiagnostic))
        self.createPrescription_window.saveButton.clicked.connect(lambda : self.saveMedsButtonHandler(cnp_pacient))
        self.createPrescription_window.listaMedicamenteWidget.itemClicked.connect(lambda : self.listMedsItemClickedHandler(idPacientDiagnostic))


    # loads the createPrescriptionWindow page
    def load_createPrescriptionWindow(self, cnp_pacient):
        if (self.patientHistory_window.listaDiagnosticeWidget.currentItem() != None):
            self.createPrescription_window.setupUi(self.window)

            dataDiagnostic = self.patientHistory_window.listaDiagnosticeWidget.currentItem().text().split(", ")[-1]

            all_meds = model.getAllMeds()

            self.createPrescription_window.numeMedicamentComboBox.clear()
            for med in all_meds:
                self.createPrescription_window.numeMedicamentComboBox.addItem(med[0])

            idPacientDiagnostic = model.getIDdiagnosticFromDate(dataDiagnostic)

            self.createPrescription_window.listaMedicamenteWidget.clear()
            self.loadMedsForPatientwithID(cnp_pacient, idPacientDiagnostic)

            # sigals and slots
            self.createPrescription_window.adugaMedicamentButton.clicked.connect(lambda: self.addMedHandler(cnp_pacient, idPacientDiagnostic))
            self.createPrescription_window.editareMedicamentButton.clicked.connect(lambda : self.updateMedHandler(cnp_pacient, idPacientDiagnostic))
            self.createPrescription_window.stergereMedicamentButton.clicked.connect(lambda : self.deleteMedHandler(cnp_pacient, idPacientDiagnostic))
            self.createPrescription_window.saveButton.clicked.connect(lambda : self.saveMedsButtonHandler(cnp_pacient))
            self.createPrescription_window.listaMedicamenteWidget.itemClicked.connect(lambda : self.listMedsItemClickedHandler(idPacientDiagnostic))


    # loads the createAppointmentWindow page 
    def load_createAppointmentWindow(self):
        self.createAppointment_window.setupUi(self.window)

        all_patients = model.getListPatients(self.emailMedicLogged,self.passwordMedicLogged)
        # populare patient combobox
        self.createAppointment_window.pacientProgramareComboBox.clear()
        for patient in all_patients:
            self.createAppointment_window.pacientProgramareComboBox.addItem(patient[0])

        all_tip_control = model.getControlTypes(self.emailMedicLogged, self.passwordMedicLogged)
        # populate control type combobox
        self.createAppointment_window.tipControlComboBox.clear()
        for tip_control in all_tip_control:
            self.createAppointment_window.tipControlComboBox.addItem(tip_control[0])

        self.loadAppointmentsForMedic()

        # signal and slots
        self.createAppointment_window.agadugaProgramareButton.clicked.connect(self.addAppointmentHandler)
        self.createAppointment_window.editareProgramareButton.clicked.connect(self.updateAppointmentHandler)
        self.createAppointment_window.stergereProgramareButton.clicked.connect(self.deleteAppointmentHandler)
        self.createAppointment_window.saveButton.clicked.connect(self.load_mainPageWindow)
        self.createAppointment_window.backCreareAppointmentButton.clicked.connect(self.load_mainPageWindow)
        self.createAppointment_window.listaProgramariWidget.itemClicked.connect(self.listAppointmentItemClickedHandler)


    # Pops up a warning window with a personalized text message
    def showWarning(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText(text)
        x = msg.exec_()  # this will show our messagebox


    # Handles the login operation
    def loginHandler(self):
        email = self.login_window.emailLineEdit.text()
        password = self.login_window.passwordLineEdit.text()
        
        try:
            if model.login(email, password ) == True:
                # retain the email and password of the currenntly logged medic
                self.emailMedicLogged = email
                self.passwordMedicLogged = password
                # redirect to main page of medic
                self.load_mainPageWindow()
        except Exception as e:
            self.showWarning("Logare esuata! Mai incearca!" + str(e.args))


    # Handels the creation of a new medic account
    def createAccountHandler(self):
        nume = self.createAccount_window.numeLineEdit.text()
        prenume = self.createAccount_window.prenumeLineEdit.text()
        CNP = self.createAccount_window.CNPLineEdit.text()
        telefon = self.createAccount_window.telefonLineEdit.text()
        email = self.createAccount_window.emailLineEdit.text()
        dataNasterii = self.createAccount_window.dateTimeEdit.text()
        dataNasterii = dataNasterii.split(" ")
        dataNasterii = dataNasterii[0].split("/")[-1] + "-" + dataNasterii[0].split("/")[-2] + "-" + dataNasterii[0].split("/")[-3] + " " + dataNasterii[1]
        
        nrCabinet = self.createAccount_window.nrCabinetLineEdit.text()
        parola = self.createAccount_window.parolaLineEdit.text()
        parolaConf = self.createAccount_window.parolaConfLineEdit.text()

        try:
            if parola == parolaConf:
                if model.addMedic(nume, prenume, CNP, telefon, email, dataNasterii, nrCabinet, parola) == True:
                    self.load_loginWindow()
            else:
                raise Exception("Parolele nu sunt identice!")
        except Exception as e:
             self.showWarning("Nu s-a putut crea contul!" + str(e.args))


    # Handels the creation of a new patient
    def createPatientHandler(self):
        nume = self.createPacient_window.numePacientLineEdit.text()
        prenume = self.createPacient_window.prenumePacientLineEdit.text()
        CNP = self.createPacient_window.CNPPacientLineEdit.text()
        telefon = self.createPacient_window.telefonPacientLineEdit.text()
        email = self.createPacient_window.emailPacientLineEdit.text()
        dataNasterii = self.createPacient_window.dataNasterePacientTimeEdit.text()
        dataNasterii = dataNasterii.split(" ")
        dataNasterii = dataNasterii[0].split("/")[-1] + "-" + dataNasterii[0].split("/")[-2] + "-" + dataNasterii[0].split("/")[-3] + " " + dataNasterii[1]
        sex = self.createPacient_window.sexPacientcomboBox.currentText()
        strada = self.createPacient_window.stradaPacientLineEdit.text()
        numar = self.createPacient_window.numarPacientLineEdit.text()
        localitate = self.createPacient_window.localitatePacientLineEdit.text()
        judet = self.createPacient_window.judetPacientLineEdit.text()

        try:
            if ( nume == "" or prenume == "" or CNP == "" or telefon == "" or strada == "" or localitate == "" or judet == ""):
                self.showWarning("Au ramas campuri necompletate! Doar emailul poate lipsi!")
            else:
                if model.addPatient(self.emailMedicLogged, self.passwordMedicLogged, nume, prenume, CNP, telefon, email, dataNasterii, strada, numar, localitate, judet, sex) == True:
                    self.load_mainPageWindow()
                else:
                    raise Exception("Pacientul nu s-a adaugat cu succes!")
        except Exception as e:
             self.showWarning("Nu s-a putut crea pacientul!" + str(e.args))


    # Searches a patient after his name
    def searchPatientHandler(self):
        text = self.mainPage_window.searchLineEdit.text()
        result = model.searchPatient(text, self.emailMedicLogged, self.passwordMedicLogged) 
        self.mainPage_window.listaPacientiWidget.clear()
        for pacient in result:
            QListWidgetItem(pacient[0], self.mainPage_window.listaPacientiWidget)


    # Gets patient's information and loads the patient's folder page
    def viewPatientFolderHandler(self):
        if (self.mainPage_window.listaPacientiWidget.currentItem() != None):
            pacient = self.mainPage_window.listaPacientiWidget.currentItem().text()
            cnp_pacient = pacient.split(', ')[-1]
            self.load_patientFolderWindow(model.getPatientByCNP(cnp_pacient))


    # Delete patient
    def deletePatientHandler(self):
        try:
            def myfunc(i):
                if i.text() == "&Yes":
                    model.deletePatient(self.patientFolder_window.CNPPacientLineEdit_2.text())
                    self.load_mainPageWindow()
            msg = QMessageBox()     # create an instance of it
            msg.setIcon(QMessageBox.Warning)    # set icon
            msg.setText("Vreti sa stergeti acest pacient?")     # set text
            msg.setWindowTitle("Confirmare stergere pacient")   # set title
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)     # type of buttons associated
            msg.buttonClicked.connect(myfunc)   # connect clicked signal
            msg.exec_()  # get the return value
        except Exception as e:
             self.showWarning("Nu s-a putut sterge pacientul!" + str(e.args))


    # Gets patient's information and loads the patient's history page
    def viewPatientHistoryHandler(self):
        if (self.mainPage_window.listaPacientiWidget.currentItem() != None):
            pacient = self.mainPage_window.listaPacientiWidget.currentItem().text()
            cnp_pacient = pacient.split(', ')[-1]
            self.load_patientHistoryWindow(model.getPatientDiagnostics(cnp_pacient), cnp_pacient)


    # Add a new diagnostic to the database
    def addDiagnostic(self, cnp_pacient):
        nume = self.createDiagnostic_window.numeDiagnosticLineEdit.text()
        descriere = self.createDiagnostic_window.descriereDiagnosticTextEdit.toPlainText()
        detalii_diag = self.createDiagnostic_window.detaliiDiagnosticTextEdit.toPlainText()
        data_diag = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
             idDiagnostic = model.addDiagnostic(nume, descriere)
             idPacientDiagnostic = model.addPatientDiagnostic(idDiagnostic, cnp_pacient, data_diag, detalii_diag)
             self.load_createPrescriptionWindowDiag(idPacientDiagnostic, cnp_pacient)
        except Exception as e:
            self.showWarning("Eroare la adaugarea diagnosticului!" + str(e.args))


    # Deletes diagnostic for a patient from the database
    def deleteDiagnosticHandler(self, cnp_pacient):
        if (self.patientHistory_window.listaDiagnosticeWidget.currentItem() != None):
            dateDiagnostic = self.patientHistory_window.listaDiagnosticeWidget.currentItem().text().split(", ")[-1]
            try:
                def myfunc(i):
                    if i.text() == "&Yes":
                        model.deleteDiagnostic(cnp_pacient, dateDiagnostic) 
                        self.load_patientHistoryWindow(model.getPatientDiagnostics(cnp_pacient), cnp_pacient)
                msg = QMessageBox()     # create an instance of it
                msg.setIcon(QMessageBox.Warning)    # set icon
                msg.setText("Vreti sa stergeti acest diagnostic?")     # set text
                msg.setWindowTitle("Confirmare stergere diagnostic pacient")   # set title
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)     # type of buttons associated
                msg.buttonClicked.connect(myfunc)   # connect clicked signal
                msg.exec_()  # get the return value
            except Exception as e:
                 self.showWarning("Eroare la stergerea diagnosticului!" + str(e.args))
    

    # Add a new medicine for a certain diagnostic
    def addMedHandler(self, cnp_pacient, IDpacientDiagnostic):
        nume = self.createPrescription_window.numeMedicamentComboBox.currentText()
        cantitate = self.createPrescription_window.cantitateMedicamentSoubleSpinBox.value()
        descriere = self.createPrescription_window.descriereTextEdit.toPlainText()

        try:
            model.addPrescription(IDpacientDiagnostic, nume, cantitate, descriere)
            self.loadMedsForPatientwithID(cnp_pacient, IDpacientDiagnostic)
        except Exception as e:
            self.showWarning("Eroare la adaugarea medicamentului! Ai grija sa nu adaugi acelasi medicament de doua ori.")


    # Refreshes the list of medicines
    def loadMedsForPatientwithID(self, cnp_pacient, IDpacientDiagnostic):
        self.createPrescription_window.listaMedicamenteWidget.clear()
        info = model.getMedsForPatient_IDpacientDiagnostic(cnp_pacient, IDpacientDiagnostic)
        for med in info:
            QListWidgetItem(med[0], self.createPrescription_window.listaMedicamenteWidget)
        

    # Updates a medicine for a certain diagnostic   
    def updateMedHandler(self, cnp_pacient, IDpacientDiagnostic):
        if (self.createPrescription_window.listaMedicamenteWidget.currentItem() != None):
            try:
                def myfunc(i):
                    if i.text() == "&Yes":
                        numeMedicament = self.createPrescription_window.listaMedicamenteWidget.currentItem().text().split(", ")[0]
                        cantitate = self.createPrescription_window.cantitateMedicamentSoubleSpinBox.value()
                        descriere = self.createPrescription_window.descriereTextEdit.toPlainText()
                        model.updatePrescription(IDpacientDiagnostic, numeMedicament, cantitate, descriere)
                        self.loadMedsForPatientwithID(cnp_pacient, IDpacientDiagnostic)
                msg = QMessageBox()     # create an instance of it
                msg.setIcon(QMessageBox.Warning)    # set icon
                msg.setText("Vreti sa editati acest medicament?")     # set text
                msg.setWindowTitle("Confirmare editare medicament")   # set title
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)     # type of buttons associated
                msg.buttonClicked.connect(myfunc)   # connect clicked signal
                msg.exec_()  # get the return value
            except Exception as e:
                 self.showWarning("Eroare la editare medicamentului! Ai grija sa fie selectat din lista medicamentul pe care vrei sa-l modifici.")
  

    # Deletes a medicine for a certain diagnostic
    def deleteMedHandler(self, cnp_pacient, IDpacientDiagnostic):
        if (self.createPrescription_window.listaMedicamenteWidget.currentItem() != None):
            try:
                def myfunc(i):
                    if i.text() == "&Yes":
                        numeMedicament = self.createPrescription_window.listaMedicamenteWidget.currentItem().text().split(", ")[0]
                        model.deletePrescription(IDpacientDiagnostic, numeMedicament)
                        self.loadMedsForPatientwithID(cnp_pacient, IDpacientDiagnostic)
                msg = QMessageBox()     # create an instance of it
                msg.setIcon(QMessageBox.Warning)    # set icon
                msg.setText("Vreti sa stergeti acest medicament?")     # set text
                msg.setWindowTitle("Confirmare stergere medicament")   # set title
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)     # type of buttons associated
                msg.buttonClicked.connect(myfunc)   # connect clicked signal
                msg.exec_()  # get the return value
            except Exception as e:
                 self.showWarning("Eroare la stergerea medicamentului!" + str(e.args))


    # Redirects to the patient history page      
    def saveMedsButtonHandler(self, cnp_pacient):
        self.load_patientHistoryWindow(model.getPatientDiagnostics(cnp_pacient), cnp_pacient)
           

    # When a list item is selected the fils are filled with the information of that medicine
    def listMedsItemClickedHandler(self, IDpacientDiagnostic):
        if (self.createPrescription_window.listaMedicamenteWidget.currentItem() != None):
            numeMedicament = self.createPrescription_window.listaMedicamenteWidget.currentItem().text().split(", ")[0]
            if ( numeMedicament != None ):
                vals = model.getMedInfoFromPrescription(IDpacientDiagnostic, numeMedicament)
                self.createPrescription_window.numeMedicamentComboBox.setCurrentText(vals[0])
                self.createPrescription_window.cantitateMedicamentSoubleSpinBox.setValue(float(vals[1]))
                self.createPrescription_window.descriereTextEdit.setText(vals[2])
            else:
                pass


    # Adds an appointment
    def addAppointmentHandler(self):
        model.deleteOlderAppointment()
        cnp_pacient = self.createAppointment_window.pacientProgramareComboBox.currentText().split(", ")[-1]
        tip_control = self.createAppointment_window.tipControlComboBox.currentText()
        data_programare = self.createAppointment_window.dataProgramareDateTimeEdit.text()
        data_programare = data_programare.split(" ")
        data_programare = data_programare[0].split("/")[-1] + "-" + data_programare[0].split("/")[-2] + "-" + data_programare[0].split("/")[-3] + " " + data_programare[1]
        descriere = self.createAppointment_window.descriereProgramareTextEdit.toPlainText()
        try:
            model.addAppointment(cnp_pacient, tip_control, data_programare, descriere)
            self.loadAppointmentsForMedic()
        except Exception as e:
                 self.showWarning("Eroare la adaugare programare! Ai grija sa nu adaugi de mai multe ori la pacient acelasi tip de control!" + str(e.args))


    # Updates an appointment
    def updateAppointmentHandler(self):
        model.deleteOlderAppointment()
        if (self.createAppointment_window.listaProgramariWidget.currentItem() != None):
            try:
                def myfunc(i):
                    if i.text() == "&Yes":
                        cnp_pacient = self.createAppointment_window.pacientProgramareComboBox.currentText().split(", ")[-1]
                        tip_control = self.createAppointment_window.tipControlComboBox.currentText()
                        data_programare = self.createAppointment_window.dataProgramareDateTimeEdit.text()
                        data_programare = data_programare.split(" ")
                        data_programare = data_programare[0].split("/")[-1] + "-" + data_programare[0].split("/")[-2] + "-" + data_programare[0].split("/")[-3] + " " + data_programare[1]
        
                        descriere = self.createAppointment_window.descriereProgramareTextEdit.toPlainText()
                        
                        model.updateAppointment(cnp_pacient, tip_control, data_programare, descriere)
                        
                        self.loadAppointmentsForMedic()
                msg = QMessageBox()     # create an instance of it
                msg.setIcon(QMessageBox.Warning)    # set icon
                msg.setText("Vreti sa editati acesta programare?")     # set text
                msg.setWindowTitle("Confirmare editare programare")   # set title
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)     # type of buttons associated
                msg.buttonClicked.connect(myfunc)   # connect clicked signal
                msg.exec_()  # get the return value
            except Exception as e:
                 self.showWarning("Eroare la editare programarii! Ai grija sa fie selectat din lista programarea pe care vrei sa o modifici.")


    # Deletes an appointment
    def deleteAppointmentHandler(self):
        model.deleteOlderAppointment()
        if (self.createAppointment_window.listaProgramariWidget.currentItem()  != None):
            try:
                def myfunc(i):
                    if i.text() == "&Yes":
                        cnp_pacient = self.createAppointment_window.listaProgramariWidget.currentItem().text().split(', ')[1]
                        data_programare = self.createAppointment_window.listaProgramariWidget.currentItem().text().split(', ')[2]
                        
                        model.deleteAppointment(cnp_pacient, data_programare)
                        
                        self.loadAppointmentsForMedic()
                msg = QMessageBox()     # create an instance of it
                msg.setIcon(QMessageBox.Warning)    # set icon
                msg.setText("Vreti sa stergeti acesta programare?")     # set text
                msg.setWindowTitle("Confirmare stergere programare")   # set title
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)     # type of buttons associated
                msg.buttonClicked.connect(myfunc)   # connect clicked signal
                msg.exec_()  # get the return value
            except Exception as e:
                 self.showWarning("Eroare la sergerea programarii! Ai grija sa fie selectat din lista programarea pe care vrei sa o stregi.")


    # When an appointment is selected from the list, the fils will be auto filled with the information
    def listAppointmentItemClickedHandler(self):
        model.deleteOlderAppointment()
        if (self.createAppointment_window.listaProgramariWidget.currentItem() != None):
            nume_prenume = self.createAppointment_window.listaProgramariWidget.currentItem().text().split(', ')[0]
            cnp_pacient = self.createAppointment_window.listaProgramariWidget.currentItem().text().split(', ')[1]
            data_programare = self.createAppointment_window.listaProgramariWidget.currentItem().text().split(', ')[2]
            vals = model.getAppointmentInfo(cnp_pacient, data_programare)
            self.createAppointment_window.pacientProgramareComboBox.setCurrentText(nume_prenume + ", " + cnp_pacient)
            self.createAppointment_window.tipControlComboBox.setCurrentText(vals[0])
            self.createAppointment_window.dataProgramareDateTimeEdit.setDateTime(vals[1])
            self.createAppointment_window.descriereProgramareTextEdit.setText(vals[2])


    # Loads the list with all appointments for a doctor
    def loadAppointmentsForMedic(self):
        model.deleteOlderAppointment()
        all_appointments = model.getAllAppointments(self.emailMedicLogged,self.passwordMedicLogged)
        self.createAppointment_window.listaProgramariWidget.clear()
        for app in all_appointments:
            self.createAppointment_window.listaProgramariWidget.addItem(app[0])
