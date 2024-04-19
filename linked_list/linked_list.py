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
            if self.head == None:
                self.head = node

            else:
                temp = self.head
                while temp.next != None:
                    temp = temp.next

                temp.next = node

    node = Node(15)
    print(node.data)
    print(node.next)

    node2 = Node('Brad: 010-3333-3532')
    print(node2.data)

    node.next = node2
    print(node.next.data)

    linkedList = LinkedList()
    linkedList.head = node
    print(linkedList.head.data)
    print(linkedList.head.next.data)