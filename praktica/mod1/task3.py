nums_input = input().split()
K = int(input())
result = []
for x in nums_input:
    num = int(x)
    if num % K == 0:
        result.append(num)
print(result)