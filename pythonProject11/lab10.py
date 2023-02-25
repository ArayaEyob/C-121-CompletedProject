# 1
class identity:
    def __init__(self, name, age, emailaddress):
        self.name = name
        self.age = age
        self.email = emailaddress

    def greet(self):
        print("Hello", self.name, "Nice to meet you")

    def person(self):
        print(self.name, self.age, self.email)


person1 = identity("Matt\n", 19, "mattzaruba@gmial.com")
person1.person()
person1.greet()


# 2

class car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def cartype(self):
        print(self.model, self.color, self.year)


c1 = car("ford ranger\n", "Blue\n", 2019)
c1.cartype()


# 3

class gravity:
    def __init__(self, m, M, G, d):
        self.mass1 = m
        self.mass2 = M
        self.gravity = G
        self.distance = d

    def force(self):
        force = (self.gravity * self.mass1 * self.mass2) / (self.distance ** 2)
        print(force)


f1 = gravity(6.67 * 10 ** (-11), 5.97 * (10 ** 24), 7.35 * (10 ** 22), 3.85 * (10 ** 8))
f1.force()


# 4

class Employee:
    def __init__(self, name, gender, salary, city):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.city = city

    def data(self):
        print(self.name, self.gender, self.salary, self.city)


employee1 = Employee("Derek", "Male", 40000, "Newyork")
employee1.data()


# 5

class patient:
    def __init__(self, patient_id, name, gender, phone, address):
        self.ID = patient_id
        self.name = name
        self.gender = gender
        self.phone = phone
        self.address = address

    def data(self, new_name):
        self.name = new_name


person_1 = patient(67829, "Eric", "Male", 423_455_1235, "450 ellis ave")
new_name = "john"

person_1.data(new_name)
print(person_1.name)
