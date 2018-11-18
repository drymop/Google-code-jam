t = int(input())

for t0 in range(1,t+1):
    n, p = map(int, input().split())
    forb = sorted([input() for _ in range(p)])
    b = [False] * p
    for i in range(p-1):
        if b[i]: continue
        for j in range(i+1, p):
            if b[j]: continue
            if forb[j].startswith(forb[i]):
                b[j] = True
            else:
                break
    forb = [2 ** (n-len(forb[i])) for i in range(len(forb)) if not b[i]]
    print('Case #%d: %d' % (t0, 2**n - sum(forb)))