s = input()
a = ""
b = ""
c = ""
space_count = 0

for ch in s:
    if ch == ' ':
        space_count += 1
    elif space_count == 0:
        a += ch
    elif space_count == 1:
        b += ch
    else:
        c += ch

num1 = int(a)
num2 = int(b)
num3 = int(c)


if num1 <= num2 <= num3 or num3 <= num2 <= num1:
    print(num2)
elif num2 <= num1 <= num3 or num3 <= num1 <= num2:
    print(num1)
else:
    print(num3)