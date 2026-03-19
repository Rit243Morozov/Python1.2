line = input().strip()
zero = 0
one = 0
position = 0
while position < len(line):
    if line[position] == '0':
        zero += 1
    elif line[position] == '1':
        one += 1
    position += 1
if zero == one:
    print('yes')
else:
    print('no')