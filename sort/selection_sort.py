import numpy as np
np.random.seed(41)
V = [*np.random.randint(1, 100, 10)]
print(V)

for i in range(len(V) - 1):     # 0부터 마지막 전까지
    min = i
    for j in range(i + 1, len(V)):
        if V[j] < V[min]:
            min = j

    V[i], V[min] = V[min], V[i]

print(V)
