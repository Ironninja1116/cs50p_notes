# Section 2 Notes Segment 2

#pritning a list
'''
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(students[i])

for student in students:
    print(student)
'''

#dictionary syntax, key: value  dictname[key] = value
'''
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep=", ")
'''

#list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Hermione", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")