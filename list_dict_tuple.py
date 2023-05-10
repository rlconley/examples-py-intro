animals = {
    "Nutmeg": "brown dog",
    "Frankie": "frenchie",
    "Steve": "guy",
    "Penelope": "chicken",
    "Luke": "big dog",
    "Sully": "cat",
    "Yoshi": "cat",
    "Fitz": "longhaired cat",
}

print(animals.items())

for pet in animals.items():
    print(pet[0] + "is a " + pet[1])

for name in animals.keys():
    print(name)

for species in animals.values():
    print(species)
