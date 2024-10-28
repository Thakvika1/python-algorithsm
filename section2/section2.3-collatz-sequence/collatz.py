def solve(n) :
    if n == 1 :
        return [1]
    if n % 2 == 0 :
        return [n] + solve(n // 2)
    if n % 2 != 0 :
        return [n] + solve(n * 3 + 1)
    
N =int(input())
s = solve(N)
print(len(s))
print(" ".join(map(str, s)))
