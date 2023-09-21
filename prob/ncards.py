import random

n = int(input())
N = 1000
avg = 0
for _ in range(N):
    whites = random.sample(range(2*n), k=n)
    res = [0 for _ in range(2*n)]
    for i in whites:
        res[i] = 1
    assert sum(res) == n
    cnt = 0
    for i in range(2*n-1):
        if res[i] != res[i+1]:
            cnt += 1
    avg += cnt / N
print(avg)
print(n)
