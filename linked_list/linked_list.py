if __name__ == '__main__':
    ## 링크드 리스트 정의
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, node):
            if self.head is None:
                self.head = node

            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next

                temp.next = node

        def print(self):
            temp = self.head
            while temp is not None:
                print(temp.data, '-> ', end='')
                temp = temp.next

            print('None')

        def unpacked_print(self):
            temp = self.head
            while temp is not None:
                print(*temp.data.keys(), '-> ', end='')
                temp = temp.next
            print('None')

        def find(self, key):
            temp = self.head
            while temp is not None:
                if key in temp.data.keys():
                    break

                temp = temp.next

            return temp

        def pop(self):  # 마지막(tail) node 꺼내기
            if self.head is None:
                return None

            prev = self.head
            temp = self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next

            if prev is temp:
                self.head = None

            else:
                prev.next = None

            return temp

        # pop_pos 기능 추가하기
        def pop_pos(self, pos):
            if self.head is None:   # head 없으면 None
                return None

            if pos < 0:   # 매개변수로 들어온 위치값이 0보다 작으면 None
                return None

            temp = self.head
            if pos == 0:
                self.head = temp.next
                return temp

            prev = temp
            temp_pos = 0
            while temp.next is not None:
                prev = temp
                temp = temp.next
                temp_pos += 1
                if temp_pos == pos:
                    prev.next = temp.next
                    return temp

            return None

    node = Node(15)
    print(node.data)
    print(node.next)

    node2 = Node('Brad: 010-3333-3532')
    print(node2.data)

    node.next = node2
    print(node.next.data)

    linkedList = LinkedList()
    linkedList.print()

    linkedList.append(Node(1))
    linkedList.print()

    linkedList.append(Node(2))
    linkedList.print()

    # 꽃말 링크드 리스트 구현
    flower_list = LinkedList()
    flower_list.print()

    flower_list.append(Node({'구기자': '희생'}))
    flower_list.append(Node({'꽈리': '약함, 수줍음'}))
    flower_list.append(Node({'과꽃': '변화, 추억'}))
    flower_list.print()
    flower_list.unpacked_print()

    flower_node = flower_list.find('꽈리')
    print(flower_node.data.keys())
    print(flower_node.data.values())
    print(*flower_node.data.keys(), ':', *flower_node.data.values())

    # pop함수 테스트
    print(flower_list.pop().data)
    print(flower_list.pop().data)
    print(flower_list.pop().data)

    # pop_pos함수 테스트
    flower_list.append(Node({'구기자': '희생'}))
    flower_list.append(Node({'꽈리': '약함, 수줍음'}))
    flower_list.append(Node({'과꽃': '변화, 추억'}))

    flower_node = flower_list.pop_pos(3)
    flower_list.print()