data = [(1, 90), (2, 56), (1, 80), (2, 89), (3, 55), (1, 45)]

students = {}

for rollno, marks in data:
     lst = students.get(rollno, [])
     lst.append(marks)
     students[rollno] = lst

for rollno, markslist in students.items():
     total = sum(markslist)
     print(f"{rollno:2}  {total:3}   {total/len(markslist):5.2f}")