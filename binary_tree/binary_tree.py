class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, node: Node):
        if self.root is None:
            self.root = node   # 최초 노드
        else:
            curr = self.root
            while True:
                if node.key < curr.key:     # 현재 노드보다 작으면
                    if curr.left is None:
                        curr.left = node    # 더 작은 수가 없는 경우, 현재 노드의 왼쪽(작은 수)에 셋팅 (가장 하위 노드가 됨)
                        break

                    else:
                        curr = curr.left    # 더 작은 수가 있는 경우, 현재 노드를 왼쪽(작은 수)으로 옮김

                elif node.key > curr.key:   # 현재 노드보다 크면
                    if curr.right is None:
                        curr.right = node  # 더 큰 수가 없는 경우, 현재 노드의 오른쪽(큰 수)에 셋팅 (가장 하위 노드가 됨)
                        break

                    else:
                        curr = curr.right   # 더 큰 수가 있는 경우, 현재 노드를 오른쪽(큰 수)로 옮김

    def print(self, node: Node):
        if node.left:   # 왼쪽(작은 수)가 존재하면 출력
            self.print(node.left)
        print(node.key, end=' ')

        if node.right:   # 오른쪽(큰 수)가 존재하면 출력
            self.print(node.right)

    def find(self, key):
        if self.root is None:
            print('No node')

        else:
            curr = self.root
            while True:
                if key < curr.key:
                    if curr.left is None:   # 매개변수의 값이 현재 노드값보다 작으면 왼쪽(작은 수)을 탐색하는데, 없으면 None 반환
                        print('No node')
                        return None

                    else:
                        curr = curr.left   # 매개변수의 값이 현재 노드값보다 작으면 왼쪽(작은 수)으로 이동

                elif key > curr.key:
                    if curr.right is None:   # 매개변수의 값이 현재 노드값보다 크면 오른쪽(큰 수)을 탐색하는데, 없으면 None 반환
                        print('No node')
                        return None

                    else:
                        curr = curr.right   # 매개변수의 값이 현재 노드값보다 크면 오른쪽(큰 수)으로 이동

                else:
                    return curr.key     # 매개변수와 동일한 값 찾음.

    def remove(self, key):
        if self.root is None:
            print('No node')

        else:
            curr: Node = self.root
            prev: Node = self.root
            while True:
                if key < curr.key:
                    if curr.left is not None:
                        prev = curr
                        curr = curr.left

                    else:
                        print('No node')
                        break

                elif key > curr.key:
                    if curr.right is not None:
                        prev = curr
                        curr = curr.right

                    else:
                        print('No node')
                        break

                elif curr.key is key:
                    if curr.left is None:   # 3, 16, 40, 60, 63, 67, 95
                        if curr is prev:
                            self.root = curr.right

                        elif curr is prev.left:     # 3(<-11), 60(<-70), 63(<-65)
                            prev.left = curr.right

                        elif curr is prev.right:    # 16(11->), 40(30->), 67(65->), 95(70->)
                            prev.right = curr.right

                    elif curr.left.right is None:   # 11, 30, 65
                        if curr is prev:
                            self.root = curr.left

                        elif curr is prev.left:     # 11(<-22), 30(<-56)
                            prev.left = curr.left
                            curr.left.right = curr.right

                        elif curr is prev.right:    # 65(60->)
                            prev.right = curr.left
                            curr.left.right = curr.right

                    else:   # 22, 56, 70
                        prev2: Node = curr.left
                        curr2: Node = curr.left.right
                        while curr2.right is not None:
                            prev2 = curr2
                            curr2 = curr2.right

                        prev2.right = curr2.left
                        curr2.left = curr.left
                        curr2.right = curr.right

                        if curr is prev:    # 56
                            self.root = curr2

                        elif curr is prev.left:     # 22(<-30)
                            prev.left = curr2

                        elif curr is prev.right:    # 70(<-56)
                            prev.right = curr2

                    return curr.key


if __name__ == '__main__':
    # nd = Node(33)
    # print(nd.key)
    #
    # print(nd.left)
    # print(nd.right)
    # childR = Node(35)
    # childL = Node(32)
    #
    # nd.right = childR
    # nd.left = childL
    # print(nd.left.key)
    # print(nd.right.key)

    bst=BSTree()
    bst.insert(Node(56))
    bst.insert(Node(30))
    bst.insert(Node(70))
    bst.insert(Node(60))
    bst.insert(Node(95))
    bst.insert(Node(65))
    bst.insert(Node(63))
    bst.insert(Node(67))
    bst.insert(Node(22))
    bst.insert(Node(40))
    bst.insert(Node(11))
    bst.insert(Node(3))
    bst.insert(Node(16))

    bst.print(bst.root)
    print()
    # print(bst.find(56))
    bst.remove(56)
    bst.print(bst.root)