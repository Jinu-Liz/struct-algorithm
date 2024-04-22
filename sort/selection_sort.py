import numpy as np
np.random.seed(41)
V = [*np.random.randint(1, 100, 10)]
print(V)

for i in range(len(V) - 1):     # 0부터 마지막 전까지
    min = i
    for j in range(i + 1, len(V)):  # 다음 숫자부터 마지막 전까지
        if V[j] < V[min]:   # 최소값을 임시 변수에 담아둠
            min = j

    V[i], V[min] = V[min], V[i]     # 최소값과 자리 변경

print(V)
