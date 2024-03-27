class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class NodeManage:
    def __init__(self, value):
        self.head = Node(value)

    def show(self):
        node = self.head

        while node:
            print(node.value)
            node = node.next

    def insert(self, value):
        node = self.head

        while node.next:
            node = node.next

        node.next = Node(value)

    def remove(self, value):
        node = self.head

        if value == node.value:
            self.head = node.next
            del node

        else:
            while node.next:
                if node.next.value == value:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next


linkedlist = NodeManage("a")
linkedlist.show()
print("---")
linkedlist.insert("b")
linkedlist.insert("c")
linkedlist.insert("d")
linkedlist.insert("e")
linkedlist.show()

print("\n")
linkedlist.remove("c")
linkedlist.insert("f")
linkedlist.show()
