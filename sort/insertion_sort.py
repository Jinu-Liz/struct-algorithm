import numpy as np
np.random.seed(51)
V = [*np.random.randint(1, 100, 100)]
print(V)

for i in range(1, len(V)):
    for j in range(i - 1, -1, -1):  # 맨 뒤에서부터 0까지 돌면서 작으면 자리 변경
        if V[j + 1] < V[j]:
            V[j + 1], V[j] = V[j], V[j + 1]
        else:
            break

print(V)