class Person:
    def __init__(self, age, sex, blood_pressure, cholesterol, heart_rate, has_disease):
        self.age = age
        self.sex = sex
        self.blood_pressure = blood_pressure
        self.cholesterol = cholesterol
        self.heart_rate = heart_rate
        self.has_disease = has_disease

    def __str__(self):
        return f"Age: {self.age} | Sex: {self.sex} | Blood pressure: {self.blood_pressure} | Cholesterol: " + \
               f"{self.cholesterol} | Heart rate: {self.heart_rate}| Has disease: {self.has_disease}"

    def __repr__(self):
        return f"Age: {self.age} | Sex: {self.sex} | Blood pressure: {self.blood_pressure} | Cholesterol: " + \
               f"{self.cholesterol} | Heart rate: {self.heart_rate}| Has disease: {self.has_disease}"


class Data:
    def __init__(self, people, bounds):
        self.people = people
        self.bounds = bounds
    
    def __str__(self):
        str = ""

        for person in self.people:
            str += person.__str__() + "\n"

        return str + f"\nBounds: {self.bounds}\n"
