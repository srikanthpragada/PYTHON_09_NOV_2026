def extract_digits(st: str) -> str:
    digits = []
    for c in st:
        if c.isdigit():
            digits.append(c)

    return "".join(digits)


names = ['Python 3', 'Java 25', 'c', 'C# 20', 'JavaScript 2025']

for cnt in map(extract_digits, names):
    print(cnt)

for cnt in map(len, names):
    print(cnt)
