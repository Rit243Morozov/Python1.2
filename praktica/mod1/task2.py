N = int(input())
numbers = list(range(N, N * N + 1))
roots = []
for x in numbers:
    roots.append(x ** 0.5)
print(numbers)
print(roots)