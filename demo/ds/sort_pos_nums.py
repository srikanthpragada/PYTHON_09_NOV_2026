# Accept numbers until 0 is given and sort and display only positive numbers
nums = []
while True:
    num = int(input("Enter number [0 to stop]:"))
    if num == 0:
        break
    if num > 0:
        nums.append(num)

nums.sort()
for n in nums:
    print(n)
