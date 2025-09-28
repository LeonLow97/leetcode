class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # to print out the singly linked list
    def print_list(self):
        node = self.head
        while node is not None:
            print(node.val, end=' -> ')
            node = node.next
        print()

    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False

SLL = SinglyLinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node3

SLL.head = node1
SLL.tail = node4

print(SLL.has_cycle())

