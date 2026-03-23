N = int(input())
names = []
for _ in range(N):
    names.append(input())

uni = []
for name in names:
    length = len(name)
    found = False
    for item in uni:
        if len(item) == length:
            found = True
            break
    if not found:
        uni.append(name)

print(names)
print(uni)