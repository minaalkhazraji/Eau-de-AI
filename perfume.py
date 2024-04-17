class Perfume:
    def __init__(self, name, notes, price, occasions):
        self.name = name
        self.notes = set(notes) #create a set of a bunch of notes
        self.price = price
        self.occasions = set(occasions)