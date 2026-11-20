st = "how do you do today"

chars = {}

for c in sorted(set(st)):
    chars[c] = st.count(c)


print(chars)