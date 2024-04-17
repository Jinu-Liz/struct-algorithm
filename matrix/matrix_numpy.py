import numpy as np

if __name__ == '__main__':
    # 행렬
    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[1, 2]])
    C = np.array([[1], [2]])

    print(A)
    print(B)
    print(C)

    # 행렬의 모양
    print(A.shape)
    print(B.shape)
    print(C.shape)

    # 행렬의 덧셈, 뺄셈, 스칼라 배
    A = np.array([[1, 2]])
    B = np.array([[3, 4]])
    print(A + B)
    print(A - B)

    C = np.array([[1, 2],
                  [3, 4]])
    D = np.array([[5, 6],
                  [7, 8]])
    print(C + D)
    print(C - D)
    print(2 * C)

    # 행렬의 곱셈
    A = np.array([[1, 2]])
    B = np.array([[3, 4],
                  [5, 6]])
    print(A @ B)

    A = np.array([[1],
                  [2]])
    B = np.array([[3, 4]])
    print(A @ B)

    C = np.array([[1, 2]])
    D = np.array([[1],
                  [2]])
    print(C @ D)

    # 행렬의 전치
    A = np.array([[1, 2]])
    print(A.T)      # 전치
    print(A.T.T)    # 원래대로
    print(A.transpose())    # A.T와 같음
    B = np.array([[1, 2],
                  [3, 4]])
    print(B.T)

    # 1 X 2 행렬의 전치 행렬과의 곱
    A = np.array([[1, 2]])
    print(A.T)
    print(A @ A.T)