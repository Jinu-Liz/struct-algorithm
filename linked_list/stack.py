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
        if self.head is None:  # head 없으면 None
            return None

        if pos < 0:  # 매개변수로 들어온 위치값이 0보다 작으면 None
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


if __name__ == '__main__':
    class Stack:
        def __init__(self, ll):
            self.stack = ll

        def push(self, x):
            self.stack.append(Node(x))

        def pop(self):
            return self.stack.pop()

        def show(self):
            return self.stack.print()

        def not_empty(self):
            return self.stack.head

    stack = Stack(LinkedList())
    for idx in range(1, 6):
        stack.push('x'+str(idx))

    stack.show()

    while stack.not_empty():
        print(stack.pop())
        stack.show()

    stack.show()