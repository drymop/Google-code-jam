Nmax = 2 * 100000 + 1
mod = 1000000007

fact = [None] * (Nmax)
fact[0] = 1
for i in range(1, Nmax):
    fact[i] = fact[i-1] * i % mod

def inv(x):
    x = x % mod
    return pow(x, mod-2, mod)

def choose(n, k):
    return fact[n] * inv(fact[k]*fact[n-k]) % mod


t = int(input())
for t0 in range(1, t+1):
    n, m = map(int, input().split())
    n *= 2
    b = True
    s = fact[n]
    for k in range(1, m+1):
        t = choose(m, k) * (1 << k) % mod
        t = t * fact[n-k] % mod
        if b:
            s -= t
        else:
            s += t
        s %= mod
        b = not b
    print('Case #%d: %d' % (t0, s))