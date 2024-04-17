if __name__ == '__main__':
    def func(*args):    # 매개변수를 튜플로 묶어준다.
        print(args)

    func(1, 2, 4, 5)

    l = [5, 6, 7, 8]
    func(*l)

    # *l  # 오류
    print([*l])     # list
    print(*l,)  # tuple
    print({*l})     # set

    # **kwargs 매개변수 이해하기
    def func_kwargs(**kwargs):  # dict로 묶어준다.
        print(kwargs)

    func_kwargs(americano=1500, caffe_latte=2000, espresso=1500)
    menu = {'americano': 1500, 'caffe_latte': 2000, 'espresso': 1500}
    func_kwargs(**menu)     # dict의 경우, **를 붙이면 풀어진다.