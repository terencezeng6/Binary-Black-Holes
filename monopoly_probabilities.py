import matplotlib.pyplot as plt
import numpy as np

tests = 30

chances = [0, 0] + ["." for i in range(tests-1)]
dice = [0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

def dp(x):
    if chances[x] != ".":
        return chances[x]
    res = dice[x] if x <= 12 else 0
    for i in range(2, min(12, x)):
        res += dice[i] * dp(x-i)
    chances[x] = res
    return res

dp(tests)
dp(tests-1)

for i in range(tests):
    print("Distance from square = ", i, ": ", round(chances[i], 4) , "% chance of landing")
    
a = [x for x in range(len(chances))]
plt.plot(a, chances[a])
