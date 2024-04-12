if __name__ == '__main__':
    # 한번에 데이터가 담긴 list 초기화
    eggs = ['egg0', 'egg1', 'egg2', 'egg3', 'egg4', 'egg5']
    print('eggs :', eggs)

    # list 생성 후 하나씩 데이터를 담기
    eggs_each = []
    eggs_each.append('egg0')
    eggs_each.append('egg1')
    eggs_each.append('egg2')
    eggs_each.append('egg3')
    eggs_each.append('egg4')
    eggs_each.append('egg5')
    print('eggs_each :', eggs_each)

    # 하나씩 데이터 꺼내기
    egg = eggs_each.pop()

    # for문을 사용한 데이터 담기
    eggs_for = []
    for idx in range(6):
        eggs_for.append('egg' + str(idx))

    print('eggs_for :', eggs_for)

    # for문을 사용한 데이터 꺼내기
    for egg in eggs_for:
        print('egg :', 'boil', egg)

    # for-in 형식 : range 함수
    print('0 ~ 10 미만')
    for i in range(10):
        print(i)

    print('0 ~ 10 미만, 2마다')
    for i in range(0, 10, 2):
        print(i)

    print('10 ~ 0 초과, -3마다')
    for i in range(10, 0, -3):
        print(i)

    # 리스트 내포 : 리스트 안에 for-in문을 넣어 생성이 편리
    inner_list = [i for i in range(10)]
    print('inner_list :', inner_list)
