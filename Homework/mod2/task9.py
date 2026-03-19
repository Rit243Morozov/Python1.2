phone = input().strip()
clean = ''
for symbol in phone:
    if symbol == '+' or (symbol >= '0' and symbol <= '9'):
        clean += symbol
print(clean)