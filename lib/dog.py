 #!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed="Beagle", age=0):
        self.name = name
        self.breed = breed
        self.age = age

    # name property
    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # breed property
    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)

    # age property
    def get_age(self):
        return self._age

    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 30:
            self._age = age
        else:
            print("Age must be between 0 and 30.")

    age = property(get_age, set_age)
