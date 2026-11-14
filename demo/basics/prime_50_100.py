# Print prime numbers from 50 to 100

for n in range(51, 100, 2):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            break
    else:
        print(n, end  = ' ')


