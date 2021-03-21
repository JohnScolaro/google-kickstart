import sys

def get_goodness(string):
    i = 0
    l = len(string) // 2
    rev = string[::-1]
    for x in range(l):
        if string[x] != rev[x]:
            i += 1
    return i

a = []
for line in sys.stdin:
    a.append(line.strip())



# Num tests
# Num letters, Goodness score
# String

a = a[1:]

for x in range(0, len(a), 2):
    k = int(a[x].split(' ')[-1])
    goodness = get_goodness(a[x+1])

    print("Case #{}: {}".format(x//2 + 1, abs(k - goodness)))