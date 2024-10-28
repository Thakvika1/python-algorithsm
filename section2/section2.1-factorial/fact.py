def fact(n) :
    result = 1
    while n != 0 :
        result *= n 
        n -= 1
    return result

N = int(input())

import time 
start = time.time()

print(fact(N))

end = time.time()
print(end - start)