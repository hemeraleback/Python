Adults = int(0)
Minor = int(0)
Stop = str('y')

while Stop == 'y':

    Name = str(input("Enter the Name: "))
    Age = int(input("Enter the age: "))

    if Age > 18:
        Adults = Adults + 1
    elif Age < 18:
        Minor = Minor + 1
    Stop = (input("Do You want to add other people? [y/n]"))

print("There are ", Adults, " adults, and ", Minor, " minor")