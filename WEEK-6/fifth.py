file = open("Marks.Data", "w")
n = int(input("Enter number of Students: "))

for i in range(n):
    roll = input("Enter roll no: ")
    name =  input("Enter Name: ")
    marks = input("Enter Marks: ")
    file.write(roll + " " + name + " " + marks + "\n")

file.close()

print("Student details Saved!")