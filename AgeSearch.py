people = [
    {
        "name": "Anna",
        "age": 28
    },
    {
        "name": "Erik",
        "age": 35
    },
    {
        "name": "Maria",
        "age": 42
    },
    {
        "name": "Lars",
        "age": 19
    },
    {
        "name": "Sofia",
        "age": 55
    }
]

name = input('name > ').lower()
output = []

for person in people:
    if person["name"] == name:
        output.append(person["name"] + " " + str(person["age"]))
if len(output) == 0:
    print("no one found")
else:
    print(output)
