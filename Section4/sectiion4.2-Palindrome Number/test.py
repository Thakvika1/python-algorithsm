def sumn(n) :
    cnt = 1
    sqrtn = int(n**0.5)
    for i in range(2, sqrtn + 1) :
        if n % i == 0 :
            cnt += i
    s = cnt * 6
    return s

N = int(input())
print(sumn(N))