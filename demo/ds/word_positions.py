# Take a string and display positions for each word

st = "how do you do today and how did you do yesterday"
words = st.split(" ")
word_positions = {}

for word in words:
    lst = word_positions.get(word, [])
    if len(lst) == 0:
        lst.append(st.find(word))    # look for first occurrence
    else:
        last_position = max(lst)
        lst.append(st.find(word, last_position + 1)) # look for next occurrent after the last one

    word_positions[word] = lst

print(word_positions)
