t = int(input())
for t0 in range(1, t+1):
    n = int(input())
    score = input()

    s = 0
    k = (n+1) // 2
    for i in range(k):
        s += int(score[i])
    m = s
    for i in range(k,n):
        s += int(score[i]) - int(score[i-k])
        m = max(m, s)
    print('Case #%d: %d' % (t0, m))