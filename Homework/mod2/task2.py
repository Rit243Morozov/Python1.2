v = 0
d = 0
m = 1
for c in input():
    if c == '.':
        d = 1
    elif d == 0:
        v = v * 10 + int(c)
    else:
        m = m * 10
        v = v + int(c) / m

p = 4 * v
a = v * v
g = v * 1.414213562

def r(x):
    if x >= 0:
        return int(x * 100 + 0.5)
    return int(x * 100 - 0.5)

p = r(p)
a = r(a)
g = r(g)

def f(x):
    t = x // 100
    h = x % 100
    if h < 10:
        return str(t) + '.0' + str(h)
    return str(t) + '.' + str(h)

print(f(p) + ', ' + f(a) + ', ' + f(g))