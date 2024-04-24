class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

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


if __name__ == '__main__':
    nd = Node(33)
    print(nd.key)

    print(nd.left)
    print(nd.right)
    childR = Node(35)
    childL = Node(32)

    nd.right = childR
    nd.left = childL
    print(nd.left.key)
    print(nd.right.key)

    bst = BSTree()
    bst.insert(Node(56))
    bst.insert(Node(30))
    bst.insert(Node(70))
    bst.insert(Node(60))
    bst.insert(Node(95))
    bst.insert(Node(65))
    bst.insert(Node(63))
    bst.insert(Node(67))
    bst.insert(Node(33))
    bst.insert(Node(27))

    bst.print(bst.root)