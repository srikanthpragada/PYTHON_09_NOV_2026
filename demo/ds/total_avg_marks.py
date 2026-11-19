data = "95,56,87,66"
marks = data.split(",")

total = 0
for m in marks:
    total += int(m)

print('Total :', total, 'Average : ', total // len(marks))
