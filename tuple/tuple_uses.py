if __name__ == '__main__':
    # 튜플과 함수의 활용
    def t_func():
        return 1, 2, 3

    a = t_func()    # 튜플
    print(a)

    a, b, c = t_func()
    print(a)
    print(b)
    print(c)

    a, *b = t_func()
    print(a)
    print(b)

    a, *_ = t_func()    # 언더바('_')의 경우, 사용하지 않는다(관심없다)
    print(a)
    print(_)    # 값이 들어가고 사용할 수 있지만, 관심없을 때 사용한다.

    # 튜플, 사전, 집합 : 내포와 생성자
    t = (i for i in range(10))  # 제너레이터(generator). 일회용이다.
    print(t)
    print((type(t)))

    for i in t:
        print(i)

    for i in t:     # 앞에서 사용했으므로 사용하지 못한다.
        print(i)

    d = {('key' + str(i)): i for i in range(10)}    # dict
    print(d)
    print((type(d)))

    s = {i for i in range(10)}      # set
    print(s)
    print((type(s)))

    # 제너레이터의 경우, 사용할 때만 조금씩 뽑아서 쓴다.
    # 리스트는 한 번에 담아서 사용하기 때문에 대용량 데이터의 경우 부담이 크다.
    # 따라서 대용량 데이터의 경우, 제너레이터를 사용하여 사용하는 경우에만 조금씩 뽑아 쓰는 것이 효율적이다.