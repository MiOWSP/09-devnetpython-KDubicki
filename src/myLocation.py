class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country


loc = Location("Kamil", "Poland")
print(loc.name)
print(loc.country)
print(type(loc))