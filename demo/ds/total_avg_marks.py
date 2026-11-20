data = "95,56,87,A,66,A"
marks = data.split(",")

total = 0
count = 0
for m in marks:
    if m.isdigit():
        total += int(m)
        count += 1

print('Total :', total, 'Average : ', total // count)
