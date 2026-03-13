print("Student Grade Calculator")

name=input("Enter Student name: ")

math= float(input("Enter Math grade: "))
science= float(input("Enter Science grade: "))
english= float(input("Enter English grade: "))
average= (math + science + english) / 3

print("\nStudent Name:", name)
print("Average: ", average)

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 75:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")
