inp = input()
correct = 1
if len(inp) == 0:
    correct = 0
elif inp[0] == '-':
    correct = 0
elif inp == "0":
    correct = 0
else:
    for sym in inp:
        if not ('0' <= sym <= '9'):
            correct = 0
            break
if correct == 0:
    print("Неверный ввод")
else:
    number = int(inp)
    # двоичная
    if number == 0:
        bin_res = "0"
    else:
        bin_res = ""
        temp = number
        while temp > 0:
            bin_res = str(temp % 2) + bin_res
            temp //= 2
    # восьмеричная
    oct_res = ""
    temp = number
    while temp > 0:
        oct_res = str(temp % 8) + oct_res
        temp //= 8
    # шестнадцатеричная
    hex_res = ""
    temp = number
    while temp > 0:
        rem = temp % 16
        if rem == 10:
            hex_res = 'a' + hex_res
        elif rem == 11:
            hex_res = 'b' + hex_res
        elif rem == 12:
            hex_res = 'c' + hex_res
        elif rem == 13:
            hex_res = 'd' + hex_res
        elif rem == 14:
            hex_res = 'e' + hex_res
        elif rem == 15:
            hex_res = 'f' + hex_res
        else:
            hex_res = str(rem) + hex_res
        temp //= 16
    print(bin_res + ', ' + oct_res + ', ' + hex_res)