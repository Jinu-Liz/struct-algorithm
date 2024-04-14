if __name__ == '__main__':
    # 장보기 1
    shopping = {'apple': 3, 'pear': 2, 'hanrabong': 5, 'pineapple': 1}
    basket = []
    for fruit, quantity in shopping.items():
        plastic_bag = []
        for _ in range(quantity):       # 따로 변수를 사용하지 않는 경우, _(언더바)로 표기함.
            plastic_bag.append(fruit)
        print(plastic_bag)
        basket.append(plastic_bag)
    print(basket)

    # 장보기 2
    shopping = {'apple': 3, 'pear': 2, 'hanrabong': 5, 'pineapple': 1}
    basket = []
    for fruit, quantity in shopping.items():
        basket.append([fruit] * quantity)
    print(basket)

    # 사전과 for-in문의 활용
    # 장보기 3
    shopping = {'apple': 3, 'pear': 2, 'hanrabong': 5, 'pineapple': 1}
    basket = [ [fruit] * quantity for fruit, quantity in shopping.items() ]     # list 내부에 for-in문을 직접 사용할 수도 있다.
    print(basket)

    # 사전과 while문의 활용
    # 장보기 4
    shopping = {'apple': 3, 'pear': 2, 'hanrabong': 5, 'pineapple': 1}
    basket = []
    while shopping:
        fruit, quantity = shopping.popitem()    # tuple의 값을 이런 식으로 담을 수 있다.
        basket.append([fruit] * quantity)
    print(basket)

    # 사전으로 해시 구현하기
    hash = {}
    hash['James'] = '754-231-5342'
    hash['Ellen'] = '555-123-4251'
    hash['Bill'] = '621-236-7423'
    hash['Susan'] = '883-234-1236'

    print(hash)
    print(hash['James'])

    # 사전과 꽃말
    flower_word = {
        '과꽃': '변화, 추억',
        '꽈리': '약함, 수줍음',
        '구기자': '희생',
        '개나리': '희망'
    }

    print(flower_word['과꽃'])