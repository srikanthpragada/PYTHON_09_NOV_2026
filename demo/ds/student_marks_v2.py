data = [(1, 90), (2, 56), (1, 80), (2, 89), (3, 55), (1, 45)]

students = {}

for rollno, marks in data:
     total = students.get(rollno, 0)
     students[rollno] = total + marks 


print(students)