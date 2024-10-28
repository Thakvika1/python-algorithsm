def solve(n) :
    cnt = 1
    for i in range(1, n + 1) :
        cnt *= i 
    return cnt

N = int(input())

import time
start = time.time()

print(solve(N))

end = time.time()
print(end - start)