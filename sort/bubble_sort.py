import numpy as np
np.random.seed(31)
V = [*np.random.randint(1, 100, 10)]
print(V)
for i in range(len(V) - 1, 0, -1):  # 99부터 1까지 1씩 줄여가며
    for j in range(i):
        if V[j] > V[j + 1]:
            V[j], V[j + 1] = V[j + 1], V[j]     # 자리를 서로 교환

print(V)