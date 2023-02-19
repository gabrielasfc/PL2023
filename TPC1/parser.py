from person import Person
from data import Data


def is_sex(sex):
    return sex == "M" or sex == "F"


def is_natural_num(num):
    return all(char.isdigit() for char in num) and int(num) > 0


def is_bit(bit):
    return bit == "0" or bit == "1"


def parse_line(line, people, bounds):
    line = line.replace("\n", "").split(",")

    if len(line) == 6 and \
       is_natural_num(line[0]) and is_sex(line[1]) and is_natural_num(line[2]) and is_natural_num(line[3]) and \
       is_natural_num(line[4]) and is_bit(line[5]):
        age = int(line[0])
        sex = line[1]
        blood_pressure = int(line[2])
        cholesterol = int(line[3])
        heart_rate = int(line[4])
        has_disease = bool(int(line[5]))

        people.append(Person(age, sex, blood_pressure, cholesterol, heart_rate, has_disease))

        if age > bounds["age"]["max"]:
            bounds["age"]["max"] = age
        elif age < bounds["age"]["min"]:
            bounds["age"]["min"] = age

        if cholesterol > bounds["cholesterol"]["max"]:
            bounds["cholesterol"]["max"] = cholesterol
        elif cholesterol < bounds["cholesterol"]["min"]:
            bounds["cholesterol"]["min"] = cholesterol 


def parse(file_path):
    people = list()

    bounds = {
        "age": {
            "max": float('-inf'),
            "min": float('inf')
        },
        "cholesterol": {
            "max": float('-inf'),
            "min": float('inf')
        }
    }

    with open(file_path, 'r') as f:
        f.readline()  # ignorar header

        for line in f.readlines():
            parse_line(line, people, bounds)

    return Data(people, bounds)
