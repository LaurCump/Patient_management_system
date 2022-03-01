import pyodbc 
from datetime import datetime

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-OFSI9CL\SQLEXPRESS;'
                      'Database=Evidenta_pacienti;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


## Function to login a doctor
#  Returns True if the login is sucessful and throws an exception if the login failed
def login(email, parola):
   cursor.execute(f"SELECT Email, Parola FROM Medic WHERE Email = \'{email}\' and Parola = \'{parola}\' ");

   if len(cursor.fetchall()) == 0:
       raise Exception
   else:
       return True
   

## Function to add a new doctor in the database
#  Returns True if the medic was added successfully and throws an exception if the addition failed
def addMedic(nume, prenume, CNP, telefon, email, dataNasterii, nrCabinet, parola):
    cursor.execute("SELECT * FROM Medic")
    len_before = len(cursor.fetchall())

    cursor.execute(f"SELECT CNP FROM Medic WHERE CNP = \'{CNP}\' ")
    if len(cursor.fetchall()) != 0:
        raise Exception("CNP nu este unic!")

    cursor.execute(f"INSERT INTO Medic (Nume, Prenume, CNP, telefon, email, dataNasterii, nrCabinet, parola) VALUES (\'{nume}\', \'{prenume}\', \'{CNP}\', \'{telefon}\', \'{email}\', \'{dataNasterii}\', \'{nrCabinet}\', \'{parola}\') ")
    conn.commit()
    cursor.execute("SELECT * FROM Medic")
    len_after = len(cursor.fetchall())

    if len_before == len_after:
        raise Exception
    else:
        return True
  

## Function to add a new patient in the database
#  Returns True if the patient was added successfully and throws an exception if the addition failed
def addPatient(emailMedic, parolaMedic, nume, prenume, CNP, telefon, email, dataNasterii, strada, numar, localitate, judet, sex):
    cursor.execute("SELECT * FROM Pacienti")
    len_before = len(cursor.fetchall())

    cursor.execute(f"SELECT CNP FROM Pacienti WHERE CNP = \'{CNP}\' ")
    if len(cursor.fetchall()) != 0:
        raise Exception("CNP nu este unic!")

    cursor.execute(f"INSERT INTO Pacienti (IDmedic, Nume, Prenume, CNP, Telefon, Email, DataNasterii, Strada, Numar, Localitate, Judet, Sex) VALUES ((SELECT IDmedic FROM Medic WHERE email = \'{emailMedic}\' and parola =  \'{parolaMedic}\'), \'{nume}\', \'{prenume}\', \'{CNP}\', \'{telefon}\', \'{email}\', \'{dataNasterii}\', \'{strada}\', \'{numar}\', \'{localitate}\', \'{judet}\', \'{sex[0]}\') ")
    conn.commit()
    cursor.execute("SELECT * FROM Pacienti")
    len_after = len(cursor.fetchall())

    if len_before == len_after:
        raise Exception
    else:
        return True


## Function to get all patients with nume, prenume and CNP
#  First join between Pacienti and Medic tables
def getListPatients(emailMedic, parolaMedic):
    cursor.execute(f"SELECT P.Nume + \' \' + P.Prenume  + \', \' + P.CNP FROM Pacienti P INNER JOIN Medic M on P.IDmedic = M.IDmedic WHERE M.email = \'{emailMedic}\' and M.parola =  \'{parolaMedic}\' ORDER BY P.Nume, P.Prenume ASC ")
    return cursor.fetchall()


## Function to get the oldest patients with nume, prenume and CNP
#  Zero subquery
def getOLderPatient(emailMedic, parolaMedic):
    cursor.execute(f"SELECT P.Nume + \' \' + P.Prenume  + \', \' + P.CNP FROM Pacienti P WHERE P.DataNasterii <= ALL(SELECT DataNasterii FROM Pacienti WHERE IDmedic = (SELECT M.IDmedic FROM Medic M WHERE M.email = \'{emailMedic}\' and M.parola = \'{parolaMedic}\')) ORDER BY P.Nume, P.Prenume ASC ")
    return cursor.fetchall()


## Function to search a patient after his name
#  Second join between Pacienti and Medic tables
def searchPatient(text, emailMedic, parolaMedic):
    cursor.execute(f"SELECT P.Nume + \' \' + P.Prenume  + \', \' + P.CNP FROM Pacienti P INNER JOIN Medic M on P.IDmedic = M.IDmedic WHERE (P.Nume like \'{text}%\' or P.Prenume like \'{text}%\') and M.email = \'{emailMedic}\' and M.parola =  \'{parolaMedic}\' ORDER BY P.Nume, P.Prenume ASC ")
    return cursor.fetchall()


## Function to find the number of patients of a medic
#  Third join between Pacienti and Medic tables
def numberPatients(emailMedic, parolaMedic):
    cursor.execute(f"SELECT count(P.IDpacient) FROM Pacienti P INNER JOIN Medic M on P.IDmedic = M.IDmedic WHERE M.email = \'{emailMedic}\' and M.parola =  \'{parolaMedic}\' GROUP BY P.IDmedic HAVING count(P.IDpacient) > 0 ")
    return cursor.fetchall()[0][0]


## Function to get information of a patient that is searched after CNP
def getPatientByCNP(CNP):
    cursor.execute(f"SELECT * FROM Pacienti WHERE CNP = \'{CNP}\' ")
    return cursor.fetchall()[0]


## Function to delete information of a patient from database
def deletePatient(CNP):
    cursor.execute("SELECT * FROM Pacienti")
    len_before = len(cursor.fetchall())
    
    cursor.execute(f"DELETE FROM Pacienti WHERE CNP = \'{CNP}\' ")
    conn.commit()
    cursor.execute("SELECT * FROM Pacienti")
    len_after = len(cursor.fetchall())

    if len_before == len_after:
        raise Exception
    else:
        return True


## Function to get diagnostics of a patient from database
#  First subquery
def getPatientDiagnostics(CNP):
    cursor.execute(f"SELECT D.Nume + ', '+ convert(varchar, PD.Data_diagnosticare, 120) FROM Diagnostic D INNER JOIN PacientDiagnostic PD on D.IDdiagnostic = PD.IDdiagnostic WHERE PD.IDpacient = (SELECT IDpacient FROM Pacienti WHERE CNP = \'{CNP}\') ORDER BY D.Nume ASC" )
    return cursor.fetchall()


## Function to get all medicines
def getAllMeds():
    cursor.execute(f"SELECT Nume FROM Medicamente")
    return cursor.fetchall()


## Function to add diagnostic to database
def addDiagnostic(nume, descriere):
    cursor.execute(f"SELECT IDdiagnostic FROM Diagnostic WHERE nume = \'{nume}\' ")
    info = cursor.fetchall()
    if len(info) == 0:
        cursor.execute(f"INSERT INTO Diagnostic (Nume, Descriere) VALUES (\'{nume}\', \'{descriere}\') ")
        conn.commit()
        cursor.execute(f"SELECT IDdiagnostic FROM Diagnostic WHERE nume = \'{nume}\' ")
        info = cursor.fetchall()
        return int(info[0][0])
    else:
        return int(info[0][0])


## Function to add diagnostic for a patient to database
#  Fourth join between Pacienti and PacientDiagnostic tables
def addPatientDiagnostic(IDdiagnostic, CNP, data_diagnostic, detalii_diagnostic):
    cursor.execute(f"SELECT PD.IDpacient_diagnostic FROM PacientDiagnostic PD INNER JOIN Pacienti P on PD.IDpacient = P.IDpacient WHERE P.CNP = \'{CNP}\' and  Data_diagnosticare = \'{data_diagnostic}\' ")
    info = cursor.fetchall()
    if len(info) == 0:
        cursor.execute(f"INSERT INTO PacientDiagnostic (IDpacient, IDdiagnostic, Data_diagnosticare, Detalii_diagnostic) VALUES ((SELECT IDpacient FROM Pacienti WHERE CNP = \'{CNP}\'), (SELECT IDdiagnostic FROM Diagnostic WHERE IDdiagnostic = \'{IDdiagnostic}\'), \'{data_diagnostic}\', \'{detalii_diagnostic}\') ")
        conn.commit()
        cursor.execute(f"SELECT PD.IDpacient_diagnostic FROM PacientDiagnostic PD INNER JOIN Pacienti P on PD.IDpacient = P.IDpacient WHERE P.CNP = \'{CNP}\' and  Data_diagnosticare = \'{data_diagnostic}\' ")
        info = cursor.fetchall()
        return int(info[0][0])
    else:
        return int(info[0][0])


## Function to add medicine to prescription for a patient to database
def addPrescription(IDpacientDiagnostic, numeMedicament, cantitate, descriere):
    cursor.execute(f"INSERT INTO Retete (IDpacient_diagnostic, IDmedicament, Cantitate, Descriere) VALUES ((SELECT IDpacient_diagnostic FROM PacientDiagnostic WHERE IDpacient_diagnostic = \'{IDpacientDiagnostic}\'), (SELECT IDmedicament FROM Medicamente WHERE Nume = \'{numeMedicament}\'), \'{cantitate}\', \'{descriere}\') ")
    conn.commit()


## Function to delete medicine to prescription for a patient from database
def deletePrescription(IDpacientDiagnostic, numeMedicament):
    cursor.execute(f"DELETE FROM Retete WHERE IDpacient_diagnostic = \'{IDpacientDiagnostic}\' and IDmedicament in (SELECT IDmedicament FROM Medicamente WHERE Nume = \'{numeMedicament}\') ")
    conn.commit()


## Function to update medicine to prescription for a patient to database
def updatePrescription(IDpacientDiagnostic, numeMedicament, cantitate, descriere):
    cursor.execute(f"UPDATE Retete SET Cantitate = \'{cantitate}\', Descriere = \'{descriere}\' WHERE IDpacient_diagnostic = \'{IDpacientDiagnostic}\' and IDmedicament in (SELECT IDmedicament FROM Medicamente WHERE Nume = \'{numeMedicament}\') ")
    conn.commit()


## Gets information of a medicine from a specific prescription
#  Fifth join between Retete and Medicamente tables
def getMedInfoFromPrescription(IDpacientDiagnostic, numeMedicament):
    cursor.execute(f"SELECT M.Nume, R.Cantitate, R.Descriere FROM Retete R INNER JOIN Medicamente M on R.IDmedicament = M.IDmedicament WHERE R.IDpacient_diagnostic = \'{IDpacientDiagnostic}\' and M.Nume = \'{numeMedicament}\' ")
    return cursor.fetchall()[0]


## Function to get the names of all medicines for a patient with a given CNP and diagnostic date
#  Second subquery
def getMedsForPatient_NameDiagnostic(cnp_pacient, data_diagnostic):
    cursor.execute(f"SELECT M.Nume + \' ,\' + str(datediff(day, getdate(), M.Data_expirare)) FROM Medicamente M INNER JOIN Retete R on M.IDmedicament = R.IDmedicament WHERE R.IDpacient_diagnostic exists (SELECT Re.IDpacient_diagnostic FROM Retete Re INNER JOIN PacientDiagnostic PD on Re.IDpacient_diagnostic = PD.IDpacient_diagnostic INNER JOIN Pacienti P on PD.IDpacient = P.IDpacient WHERE PD.Data_diagnosticare =  \'{data_diagnostic}\' and P.CNP = \'{cnp_pacient}\') and datediff(day, getdate(), M.Data_expirare) > 0 ORDER BY datediff(day, M.Data_expirare, getdate()) ASC ")
    return cursor.fetchall()


## Function to get the names of all medicines for a patient with a given CNP and his diagnostic id
#  Third subquery
def getMedsForPatient_IDpacientDiagnostic(cnp_pacient, IDpacientDiagnostic):
    cursor.execute(f"SELECT M.Nume + \', \' + str(datediff(day, getdate(), M.Data_expirare)) FROM Medicamente M INNER JOIN Retete R on M.IDmedicament = R.IDmedicament WHERE R.IDpacient_diagnostic in (SELECT Re.IDpacient_diagnostic FROM Retete Re INNER JOIN PacientDiagnostic PD on Re.IDpacient_diagnostic = PD.IDpacient_diagnostic INNER JOIN Pacienti P on PD.IDpacient = P.IDpacient WHERE PD.IDpacient_diagnostic =  \'{IDpacientDiagnostic}\' and P.CNP = \'{cnp_pacient}\') ORDER BY datediff(day, M.Data_expirare, getdate()) ASC ")
    return cursor.fetchall()


## Function to delete the diagnostic of a patient
def deleteDiagnostic(CNP, data_diagnostic):
    cursor.execute("SELECT * FROM PacientDiagnostic")
    len_before = len(cursor.fetchall())

    cursor.execute(f"DELETE FROM PacientDiagnostic WHERE IDpacient in (SELECT IDpacient FROM Pacienti WHERE CNP = \'{CNP}\') and Data_diagnosticare = \'{data_diagnostic}\' ")
    conn.commit()
    cursor.execute("SELECT * FROM PacientDiagnostic")
    len_after = len(cursor.fetchall())

    if len_before == len_after:
        raise Exception
    else:
        return True


## Function to get th IDfiagnostic using the diagnostic date
def getIDdiagnosticFromDate(data_diagnostic):
    cursor.execute(f"SELECT IDpacient_diagnostic FROM PacientDiagnostic WHERE Data_diagnosticare =  \'{data_diagnostic}\'")
    return cursor.fetchall()[0][0]


## Function to get all control types 
#  Sixth join between Medic and Control tables
def getControlTypes(emailMedic, parolaMedic):
    cursor.execute(f"SELECT C.Tip FROM Control C INNER JOIN Medic M on C.IDmedic = M.IDmedic WHERE M.Email = \'{emailMedic}\' and M.Parola = \'{parolaMedic}\' ")
    return cursor.fetchall()


## Function to add an appointment for a patient to database
def addAppointment(cnp_pacient, tip_control, data_programare, detalii):
    print(data_programare)
    cursor.execute(f"INSERT INTO Programari (IDpacient, IDcontrol, Data_programare, Detalii_programare) VALUES ((SELECT IDpacient FROM Pacienti WHERE CNP = \'{cnp_pacient}\'), (SELECT IDcontrol FROM Control WHERE Tip = \'{tip_control}\'), \'{data_programare}\', \'{detalii}\') ")
    conn.commit()


## Function to delete an appointment for a patient from database
def deleteAppointment(cnp_pacient, data_programare):
    print(data_programare)
    cursor.execute(f"DELETE FROM Programari WHERE IDpacient in (SELECT IDpacient FROM Pacienti WHERE CNP = \'{cnp_pacient}\') and Data_programare = \'{data_programare}\' ")
    conn.commit()


## Function to update an appointment for a patient to database for a certain control type
def updateAppointment(cnp_pacient, tip_control, data_programare, detalii):
    print(data_programare)
    cursor.execute(f"UPDATE Programari SET Data_programare = \'{data_programare}\', Detalii_programare = \'{detalii}\' WHERE IDpacient in (SELECT IDpacient FROM Pacienti WHERE CNP = \'{cnp_pacient}\') and IDcontrol in (SELECT IDcontrol FROM Control WHERE Tip = \'{tip_control}\') ")
    conn.commit()


## Function to get all appointments from a doctor
#  Fourth subquery
def getAllAppointments(emailMedic, parolaMedic):
    cursor.execute(f"SELECT P.Nume + ' ' + P.Prenume + ', ' + P.CNP + ', ' + convert(varchar, Pr.Data_programare, 120) FROM Pacienti P INNER JOIN Programari Pr on P.IDpacient = Pr.IDpacient WHERE P.IDmedic = (SELECT IDmedic FROM Medic WHERE Email = \'{emailMedic}\' and Parola = \'{parolaMedic}\') and Pr.Data_programare > getdate() ORDER BY Pr.Data_programare ASC")
    return cursor.fetchall()


## Function to get information's of an appointment for a patient
#  Seventh join between Control, Programari and Pacienti tables
def getAppointmentInfo(cnp_pacient, data_programare):
    cursor.execute(f"SELECT C.Tip, Pr.Data_programare, Pr.Detalii_programare FROM Control C INNER JOIN Programari Pr on C.IDcontrol = Pr.IDcontrol INNER JOIN Pacienti P on Pr.IDpacient = P.IDpacient WHERE Pr.Data_programare = \'{data_programare}\' and P.CNP = \'{cnp_pacient}\' ")
    return cursor.fetchall()[0]


## Function to delete all appointment older than the current day
def deleteOlderAppointment():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(f"DELETE FROM Programari WHERE Data_programare < \'{current_date}\' ")
    conn.commit()
