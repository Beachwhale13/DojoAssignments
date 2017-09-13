import itertools

class Patients(object):
    id_generator = itertools.count(1)
    def __init__(self, name, allergies):
        self.id = next(self.id_generator)
        self.name = name
        self.allergies = allergies
        self.bed_number = 0

patient1 = Patients("Sandy", "cats")
patient2 = Patients("Kai", "kindness")
patient3 = Patients("Yao", "work")



class Hospital(object):
    def __init__(self, name):
        self.patient_list = []
        self.name = name
        self.capacity = 2
        self.beds = 1

    def admit(self, patient):
        self.patient_list.append(patient)
        if (len(self.patient_list)) > self.capacity:
            self.patient_list.pop()
            print "No Helpy Help Here", patient.name
        else:
            patient.bed_number = self.beds
            self.beds += 1
            print "Admitted:", patient.name, "is assigned bed number", self.beds
        return self

    def discharge(self, name):
        for patient in self.patient_list:
            if patient.name == name:
                patient.bed_number = 0
                self.patient_list.remove(patient)
        return self

    def display_list(self):
        for patient in self.patient_list:
            print patient.name, patient.bed_number
        return self


myHospital = Hospital("HELPy HELPy HOSPITAL")
myHospital.admit(patient1).admit(patient2).admit(patient3).display_list()
myHospital.discharge("Sandy").display_list()
print patient2.bed_number
print patient1.bed_number
