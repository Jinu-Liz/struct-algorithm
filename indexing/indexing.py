if __name__ == '__main__':
    # 문자열 처리와 임의 데이터 생성
    # 한 문자열 접근
    print('hello'[0])
    print('hello'[1])
    print('hello'[4])
    # print('hello'[5])   # 오류

    print('hello'[-0])
    print('hello'[-1])
    print('hello'[-5])
    # print('hello'[-6])   # 오류

    # 부분 문자열 접근: slicing
    print('hello'[0:1])
    print('hello'[0:2])
    print('hello'[1:3])
    print('hello'[:3])
    print('hello'[3:])
    print('hello'[:])
    print('hello'[1:4:2])
    print('hello'[::2])

    print('hello'[-3:-1])
    print('hello'[-3:])
    print('hello'[:-3])
    print('hello'[-1:-3])   # 없음
    print('hello'[4:2])     # 없음
    print('hello'[-1:-3:-1])
    print('hello'[4:2:-1])