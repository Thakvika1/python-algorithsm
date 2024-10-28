import random

SEED, MIN, MAX, N = 2022, 10, 100, 8
random.seed(SEED)
s = random.sample(range(MIN, MAX), N)

print(s)
print(sorted(s, reverse = True))
print(sorted(s))
print(sorted(s, reverse = False))
print(s)