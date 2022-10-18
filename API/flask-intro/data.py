from person import Person

names = ['Kelvin', 'Kelp', 'Kel']
ages = [19, 20, 21]

persons = list(map(lambda name, age: Person(name, age), names, ages))

# print(persons[0].showContent())
