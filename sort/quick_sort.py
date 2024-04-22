import numpy as np


def quick_sort(V, low, high):
    if low >= high:     # 하나만 남아서 정렬할 것이 없음.
        return

    key = V[high]   # pivot
    left, right = low, high - 1     # left는 가장 작은 값, right는 pivot 왼쪽
    while True:
        while V[left] < key and left < high:    # left값이 pivot 이상이 되거나, pivot 자리 이상이 될 때까지 (큰 값을 찾는다.)
            left += 1
        while V[right] > key and right > 0:    # right값이 pivot 이하가 되거나, 0이 될 때까지 (작은 값을 찾는다.)
            right -= 1

        if left >= right:   # left와 right가 같으면 교차가 되었다는 뜻.
            break

        V[left], V[right] = V[right], V[left]   # left값과 right값을 치환
        left += 1
        right -= 1

    if left < high:
        V[left], key = key, V[left]     # pivot과 치환환

    # 재귀함수를 사용
    quick_sort(V, low, left - 1)
    quick_sort(V, left + 1, high)


if __name__ == '__main__':
    np.random.seed(61)
    V = [*np.random.randint(1, 100, 10)]
    quick_sort(V, 0, len(V) - 1)
    print(V)