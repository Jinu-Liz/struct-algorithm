if __name__ == '__main__':
    # dict: 열쇠로 값 찾기
    # dict의 경우, 순서 개념이 존재하지 않는다.
    shopping = {}
    shopping['apple'] = 3
    shopping['pear'] = 2
    shopping['hanrabong'] = 5
    shopping['pineapple'] = 2
    print(shopping)

    # dict 항목 읽기 - key를 이용하여 값을 가져온다.
    print(shopping['apple'])
    print(shopping['hanrabong'])

    # dict 주요 함수
    shopping = {'apple': 3, 'pear': 2, 'hanrabong': 5, 'pineapple': 1}
    print(shopping.keys())
    print(shopping.values())
    print(shopping.items())     # 튜플(tuple) 형태

    # dict 풀어내기 1 : list
    print(list(shopping.keys()))
    print(list(shopping.values()))
    print(list(shopping.items()))

    # dict 풀어내기 2 : unpacking operator
    # 앞에 * 을 붙이면 unpacking operator. 보통 list로 받는다.
    # list(shopping.keys()) = [*shopping.keys()]
    print([*shopping.keys()])
    print([*shopping.values()])
    print([*shopping.items()])

    # tuple로 풀기
    print((*shopping.keys(),))
    print((*shopping.values(),))
    print((*shopping.items(),))

    # set으로 풀기
    print({*shopping.keys()})
    print({*shopping.values()})
    print({*shopping.items()})

    # dict와 for-in문
    for key in shopping.keys():
        print('key :', key)

    for value in shopping.values():
        print('value :', value)

    for item in shopping.items():
        print('item :', item)

    for key, value in shopping.items():
        print('tuple key:', key)
        print('tuple value:', value)