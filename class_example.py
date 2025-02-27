

def employee(name, age, **misc):
    employeedata = {}
    employeedata["name"] = name
    employeedata["age"] = age

    for key, value in misc.items():
        employeedata[key] = value

    return employeedata


class Cat():
    def __init__(self, name, color='n/a', gender='n/a'):
        self.name = name 
        self.color = color
        self.gender = gender

    @staticmethod
    def meow():
        print("meowwww")


class VillageCat(Cat):
    def __init__(self, name, color='n/a', gender='n/a'):
        super().__init__(name, color='n/a', gender='n/a')
        self.fur = Fur(color)

class Fur():
    def __init__(self, color):
        self.color = color

    def shed(self):
        print("shedding " + self.color + " fur")

