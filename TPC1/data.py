class Data:
    def __init__(self, people, bounds):
        self.people = people
        self.bounds = bounds
    
    def __str__(self):
        str = ""

        for person in self.people:
            str += person.__str__() + "\n"

        return str + f"\nBounds: {self.bounds}\n"
