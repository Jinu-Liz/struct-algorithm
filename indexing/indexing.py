import random
import string

if __name__ == '__main__':
    # 문자열 처리와 임의 데이터 생성
    hello_str = 'hello'
    # 한 문자열 접근
    print(hello_str[0])
    print(hello_str[1])
    print(hello_str[4])
    # print(str[5])   # 오류

    print(hello_str[-0])
    print(hello_str[-1])
    print(hello_str[-5])
    # print(str[-6])   # 오류

    # 부분 문자열 접근: slicing
    print(hello_str[0:1])
    print(hello_str[0:2])
    print(hello_str[1:3])
    print(hello_str[:3])
    print(hello_str[3:])
    print(hello_str[:])
    print(hello_str[1:4:2])
    print(hello_str[::2])

    print(hello_str[-3:-1])
    print(hello_str[-3:])
    print(hello_str[:-3])
    print(hello_str[-1:-3])   # 없음
    print(hello_str[4:2])     # 없음
    print(hello_str[-1:-3:-1])
    print(hello_str[4:2:-1])
    
    # 문자열 주요 함수
    print(len(hello_str))
    join1 = ','.join(['hello', 'world'])
    print(join1)
    print(join1.split(','))

    join2 = ','.join(['spiderman', 'superman', 'batman', 'aquaman'])
    print(join2)
    print(join2.split(','))

    # 임의 숫자 생성
    print(random.random())  # 랜덤 실수
    print(random.randint(0, 100))   # 범위 내의 랜덤 정수
    list = []
    for _ in range(10):
        list.append(random.random())
    print(list)

    list2 = []
    for _ in range(10):
        list2.append(random.randint(0, 10))
    print(list2)

    # 리스트 내포
    print([ random.random() for _ in range(10)])
    print([ random.randint(0, 100) for _ in range(10) ])


    # 임의 문자열 생성
    print(string.ascii_letters)     # 영어 문자열
    print(random.choices(string.ascii_letters, k=10))   # 문자열 중 10개를 랜덤으로 뽑기
    print(''.join(random.choices(string.ascii_letters, k=10)))      # 10자의 랜덤 문자열