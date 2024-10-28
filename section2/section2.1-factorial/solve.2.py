def fact(n) :
    if n == 0 :
        return 1
    else :
        return n * fact(n - 1)

import sys
sys.setrecursionlimit(10**5)


N = int(input())

import time
start = time.time()

print(fact(N))

end = time.time()
print(end - start)

