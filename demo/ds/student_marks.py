data = [(1, 90), (2, 56), (1, 80), (2, 89), (3, 55), (1, 45)]

students = {}

for rollno, marks in data:
    if rollno in students:
        students[rollno] = students[rollno] + marks
    else:
        students[rollno] = marks


print(students)