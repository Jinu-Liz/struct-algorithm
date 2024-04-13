if __name__ == '__main__':
    # 리스트로 스택 구현
    stack = []
    stack.append('x1')
    stack.append('x2')
    stack.append('x3')
    stack.append('x4')
    stack.append('x5')
    print(stack)
    print(stack.pop())

    # 리스트로 스택 구현 (class)
    class Stack:
        def __init__(self):
            self.stack = []

        def push(self, x):
            self.stack.append(x)

        def pop(self):
            return self.stack.pop()

        def show(self):
            return self.stack

        def not_empty(self):
            return len(self.stack) > 0

    stack = Stack()
    for idx in range(1, 6):
        stack.push('x' + str(idx))
    print(stack.show())

    while stack.not_empty():
        print(stack.pop())
    print(stack.show())