# 튜플의 기본젖ㄱ인 활용
if __name__ == '__main__':
    a = (1, 2, 3, 4)
    print(a)
    print(type(a))

    b = (1)
    print(b)
    print(type(b))  # 하나면 int. 콤마를 하나 이상 넣어야 튜플로 만들어진다.
    b = 1, 2, 4, 5  # 튜플로 만들어진다.
    print(b)

    c = (1,)
    print(c)
    print(type(c))  # 콤마가 있기 때문에 튜플

    # 아래 예시의 결과는 모두 동일하다. (int)
    # 튜플에서는 괄호보다 콤마가 중요.
    d, e = 5, 6
    print(d)
    print(e)

    d, e = (5, 6)
    print(d)
    print(e)

    (d, e) = 5, 6
    print(d)
    print(e)

    (d, e) = (5, 6)
    print(d)
    print(e)


    # 남은거 리스트로 묶기 : packing operator
    # '*'이 변수에 붙으면 리스트 묶기 연산자 (나머지를 모두 묶어달라)
    # d, e = 5, 6, 7  # 변수보다 값이 많기 때문에 오류
    d, *e = 5, 6, 7     # 5를 제외한 나머지는 list형태로 e에 넣는다.
    print(d)
    print(e)

    *d, e = 5, 6, 7     # 마지막 7을 제외한 나머지를 list형태로 d에 넣는다.
    print(d)
    print(e)

    d, *e, f = 5, 6, 7
    print(d)
    print(e)    # 6만 list형태로
    print(f)

    d, *e, f = 5, 6
    print(d)
    print(e)  # 처음 5와 마지막 6을 제외한 나머지를 list형태로 e에 넣는다. (넣을 값이 없으므로 빈 list)
    print(f)

    # d, *e, f = 5    # 에러

    *e, f = 5, 6
    print(e)
    *e, = 5,    # 나머지를 묶는다.
    print(e)

    # *e, = 5     # 에러
    # *e = 5,     # 에러