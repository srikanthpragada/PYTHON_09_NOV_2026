# Take numbers from user at the most 10 or until 0 is given

total = 0
for i in range(1, 11):
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    total += num

print('Total = ', total)
