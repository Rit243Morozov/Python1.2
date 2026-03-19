def fast_pow(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        return fast_pow(base * base, exp // 2)
    return base * fast_pow(base, exp - 1)

base, exp = map(int, input().split())
print(fast_pow(base, exp))