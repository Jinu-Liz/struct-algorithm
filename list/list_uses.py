if __name__ == '__main__':
    # 리스트 연산 (뺄셈/나눗셈은 없음)

    # 두 리스트 내의 값을 합쳐 하나의 리스트로 만듦. flatMap 같은 느낌
    print([1] + [2])

    # list 내에 1을 5개 넣음
    print([1] * 5)

    # 하나의 리스트로
    print(['hello'] + ['world'])

    # list 내에 hello를 3개 넣음
    print(['hello'] * 3)

    # 항목 접근
    list1 = [0, 1, 2, 3, 4]
    print('0번 : ', list1[0])
    print('1번 : ', list1[1])
    print('4번 : ', list1[4])
    # print('5번 : ', list1[5])    # 범위를 벗어났기 때문에 에러 발생

    print('-0번 : ', list1[-0])  # -0은 0과 같다.
    print('-1번 : ', list1[-1])
    print('-2번 : ', list1[-2])
    print('-5번 : ', list1[-5])
    # print('-5번 : ', list1[-6])  # 범위 벗어남

    # 부분 항목 접근 (slice)
    print('0번 ~ 1번 전', list1[0:1])
    print('0번 ~ 2번 전', list1[0:2])
    print('1번 ~ 3번 전', list1[1:3])
    print('처음 ~ 3번 전', list1[:3])
    print('3번 ~ 끝', list1[3:])
    print('처음 ~ 끝', list1[:])
    print('1부터 4 미만까지 간격 2', list1[1:4:2])
    print('매 간격 2', list1[::2])
    print('뒤에서 3번째부터 뒤에서 1번째 전까지', list1[-3:-1])
    print('뒤에서 3번째부터 끝까지', list1[-3:])
    print('처음부터 뒤에서 3번째 전까지', list1[:-3])
    print('뒤에서 1번째부터 뒤에서 3번째 전까지 (없다)', list1[-1:-3])
    print('list1[-1:-3]과 동일', list1[4:2])
    print('뒤에서 1번째부터 뒤에서 3번째 전까지 거꾸로', list1[-1:-3:-1])
    print('list1[-1:-3:-1]과 동일', list1[4:2:-1])