class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)

        else:
            node = self.root

            while 1:
                if value < node.value:
                    if node.left is None:
                        node.left = Node(value)
                        break
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(value)
                        break
                    else:
                        node = node.right

    def search(self, value):
        node = self.root

        while 1:
            if value == node.value:
                return True

            elif value < node.value:
                if node.left is None:
                    return False
                else:
                    node = node.left

            else:
                if node.right is None:
                    return False
                else:
                    node = node.right

    def preorder(self):
        def order(node):
            result.append(node.value)

            if node.left is not None:
                order(node.left)

            if node.right is not None:
                order(node.right)

        result = []
        order(self.root)
        return result

    def postorder(self):
        def order(node):
            if node.left is not None:
                order(node.left)

            if node.right is not None:
                order(node.right)

            result.append(node.value)

        result = []
        order(self.root)
        return result


tree = Tree()
tree.insert(3)
tree.insert(1)
tree.insert(9)
print(tree.search(1))
print(tree.preorder())
print(tree.postorder())
