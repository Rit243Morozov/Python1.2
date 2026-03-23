N = int(input())
names = []
for _ in range(N):
    names.append(input())

uni = []
for name in names:
    found = False
    for u in uni:
        if len(u) == len(name):
            found = True
            break
    if not found:
        uni.append(name)

print(names)
print(uni)