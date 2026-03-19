phrase = input().strip() + ' '
current_word = ''
output = ''
for symbol in phrase:
    if symbol == ' ':
        if current_word:
            output += current_word[-1]
            current_word = ''
    else:
        current_word += symbol
print(output)