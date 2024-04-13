if __name__ == '__main__':
    queue = []
    queue.append('x1')
    queue.append('x2')
    queue.append('x3')
    queue.append('x4')
    queue.append('x5')

    print(queue)
    print(queue.pop(0))
    print(queue)

    # 리스트로 큐 구현하기
    class Queue:
        def __init__(self):
            self.queue = []

        def en_queue(self, x):
            self.queue.append(x)

        def de_queue(self):
            return self.queue.pop(0)

        def show(self):
            return self.queue

        def not_empty(self):
            return len(self.queue) > 0

    queue = Queue()
    for idx in range(1, 6):
        queue.en_queue('x' + str(idx))
    print(queue.show())

    while queue.not_empty():
        print(queue.de_queue())
    print(queue.show())