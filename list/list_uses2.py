import numpy as np
import random

if __name__ == '__main__':
    # 리스트 주요 함수 : len, sort, reverse, random.shuffle
    np.random.seed(42)
    list = list(np.random.randint(0, 100, 10))      # 0 ~ 100까지 중 10개
    print(list)
    print(len(list))

    # 작은 수부터 정렬
    list.sort()
    print(list)

    # 거꾸로 뒤집기
    list.reverse()
    print(list)

    # 섞기
    random.shuffle(list)
    print(list)


    list.sort()

    # 항목 추가
    list.append(93)
    list.append(94)
    print(list)
    print(len(list))

    # 항목 꺼내기 (맨 뒤에서)
    print(list.pop())
    print(list.pop())

    # 0번째부터 꺼내기
    print(list.pop(0))
    print(list.pop(0))
    print(list)

    # 0번에 숫자 추가
    list.insert(0, 49)
    list.insert(0, 48)
    print(list)


    # 활용 예시 : 냉장고에서 사과 찾기 1
    fridge = ['apple', 'pear', 'mandarine', 'banana']
    where = fridge.index('apple')
    print('사과 위치', where)
    apple = fridge.pop(where)
    print('사과', apple)

    # 활용 예시 : 냉장고에서 사과 찾기 2 (if-in문 사용)
    fridge = ['apple', 'pear', 'mandarine', 'banana']
    if 'apple' in fridge:
        where = fridge.index('apple')
        apple = fridge.pop(where)
        print('eat', apple)

    # while문 활용
    fridge = ['apple', 'pear', 'mandarine', 'banana']
    while fridge:
        fruit = fridge.pop()
        print('eat', fruit)
    print(fridge)

    # 과일 찾기
    fridge = ['apple', 'pear', 'mandarine', 'banana']
    for fruit in fridge:
        print('find', fruit)