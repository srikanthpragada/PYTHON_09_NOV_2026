nums = [-10, 5, 4, 9, -20, 40, -50]

for n in sorted(nums):
    print(n, end=' ')

print()

for n in sorted(nums, key=abs):
    print(n, end=' ')
