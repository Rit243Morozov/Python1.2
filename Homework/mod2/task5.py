address = input()
part1 = ""
part2 = ""
part3 = ""
counter = 0
buffer = ""
for sym in address:
    if sym == '.':
        if counter == 0:
            part1 = buffer
        elif counter == 1:
            part2 = buffer
        counter += 1
        buffer = ""
    else:
        buffer += sym
if counter == 0:
    part1 = buffer
elif counter == 1:
    part2 = buffer
else:
    part3 = buffer
if part3:
    print(part3)
if part2:
    print(part2)
if part1:
    print(part1)