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