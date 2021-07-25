def reverse_text(text):
    for ch in range(len(text) - 1, -1, -1):
        yield text[ch]


for char in reverse_text("step"):
    print(char, end='')
