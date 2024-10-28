def solve(n, m) :
    mins = []
    maxs = []
    for i in range(1, n) :
        if n % i == 0 :
            mins.append(i)
    for j in range(1, m) :
        if m % j == 0 :
            maxs.append(j)
    maxn = max(mins)
    for k in range(len(maxs)) :
        if maxn == k :
            print(maxn)
    return maxn

N = int(input())
M = int(input())

import time
start = time.time()

print(solve(N, M))

end = time.time()
print(end - start)