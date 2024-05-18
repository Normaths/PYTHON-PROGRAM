science_degrees = ("Mathematics", "Physics", "Computer Science", "Engineering")
print(science_degrees[0])
print(type(science_degrees))
a = list(science_degrees)
del(a[len(science_degrees)-1])
print(a)

physical_sciences = ["Pure Mathematics"]
science_1 = "Theoretical Physics"
physical_sciences.append(science_1)
science_2 = "Theoretical Computer Science"
physical_sciences.append(science_2)
print(physical_sciences)
physical_sciences[1] = "Mathematical and Theoretical Physics"
print(physical_sciences)

name = ["Dr. Norman Mohammad Bin Sumar", "Dr. Frederick", "Dr. Alban", "Dr. Alban"]
a = set(name)
print(name)
print(a)
print(type(a))

username = []
username_1 = str(input("Please insert your username:" ))
username.append(username_1)
username_2 = str(input("Please insert your username:" ))
username.append(username_2)
username_3 = str(input("Please insert your username: "))
username.append(username_3)
sequence = [1, 2]
information = {
    "information 1" : username,
    "information 2" : sequence,
}
print(information)
print(information["information 1"])
