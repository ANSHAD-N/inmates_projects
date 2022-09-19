
#1
class Hospital:
    def __init__(self, admin, doctor, sister, department):
        self.admin = admin
        self.doctor = doctor
        self.sister = sister
        self.department = department

    def get_detail(self):
        self.admin = input("Enter admin name : ")
        self.doctor = input("Enter doctor name : ")
        self.sister = input("Enter sister  name : ")
        self.department = input("Enter department  name : ")


class Department(Hospital):

    def show_data(self):
        print("Admin : ", self.admin, "\n Doctor : ", self.doctor, "\n Sister : ", self.sister,
              "\n Department : ", self.department)


class PatientWard(Hospital):
    def __init__(self, name, age, address, disease):
        self.name = name
        self.age = age
        self.address = address
        self.disease = disease

    def get_detail(self):
        self.name = input("Enter name of patient : ")
        self.age = input("Enter age of patient : ")
        self.address = input("Enter address of patient : ")
        self.disease = input("Enter disease of patient : ")

    def show_detail(self):
        print("\n Patient name : ", self.name, "\n Patient age : ", self.age,
              "\n Patient's address : ", self.address, "\nDisease : ", self.disease)


hospital = Department('', '', '', '')
hospital.get_detail()
hospital.show_data()

patient = PatientWard('', '', '', '')
patient.get_detail()
patient.show_detail()

#2
a = {2, 1, 4, 5, 9, 7, 3, 0}
print(a)
print(len(a))
a.add(8)
print(a)
a.pop()
print(a)
b = {8, 6, 5, 44, 443, 33, 12}
print(b)
print(a-b)
print(b-a)
print(a & b)
print(a | b)
