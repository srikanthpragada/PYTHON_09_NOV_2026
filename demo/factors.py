# Take a number and display its factors

num = int(input("Enter a number :"))

factor_found = False
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(i, end = ' ')
        factor_found = True

if not factor_found:
    print('No factors found as number is prime!')



