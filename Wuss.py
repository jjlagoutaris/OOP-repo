# OOP - INHERITANCE -

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Catchphrase.exe"

    def set_age(self, param):
        self.age = param
        return self.age

    def get_attributes(self):
        attributes = [self.name, self.age]
        return attributes


class Male(Person):
    def __init__(self, name, age, chest_hair):
        super().__init__(name, age)
        self.chest_hair = chest_hair

