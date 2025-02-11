def is_prime(n) :
    if n <= 1 :
        return False
    for i in range(2, int(n**0.5) + 1 ) :
        if n % i == 0 :
            return False
    return True

def solve(n) :
    cnt = 0
    for i in range(2, n + 1) :
        if is_prime(i) :
            cnt += 1
    return cnt

N = int(input())
print(solve(N))