user_input = input()
pos = 0
while pos < len(user_input) and user_input[pos] != ',':
    pos += 1
if pos < len(user_input):
    main_str = user_input[:pos]
    char_str = user_input[pos+1:]
else:
    main_str = user_input
    char_str = ""
target = ''
for ch in char_str:
    if ch != ' ':
        target = ch
        break
counter = 0
for ch in main_str:
    if ch == target:
        counter += 1
    else:
        break
print(counter)