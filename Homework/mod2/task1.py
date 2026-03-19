z = input()
a_str = ""
b_str = ""
comm = False
for char in z:
    if char == ',':
        comm = True
    elif not comm:
        a_str += char
    else:
        b_str += char

a = int(a_str.strip())
b = int(b_str.strip())
print(a % b)