class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" <-> ")
            current = current.next
        print("None")

    def push(self, val):
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return self

    def pop(self):
        if self.head is None:
            return None
        # check length of DLL
        removedNode = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.tail = removedNode.prev
            removedNode.prev = None
            self.tail.next = None
        self.length -= 1
        return removedNode

    def shift(self):
        if self.length == 0:
            return None

        removedHead = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = removedHead.next
            self.head.prev = None
            removedHead.next = None
        self.length -= 1
        return removedHead

    def unshift(self, val):
        newHead = ListNode(val)
        if self.length == 0:
            self.head = newHead
            self.tail = newHead
        else:
            self.head.prev = newHead
            newHead.next = self.head
            self.head = newHead
        self.length += 1
        return self
    
    def get(self, index):
        if index < 0 or index > self.length - 1:
            return None
        if index == 0:
            return self.head
        elif index == self.length - 1: 
            return self.tail

        # perform binary search (better time complexity, works for DLL only)
        mid = (self.length - 1) // 2
        current = None

        if index < mid:
            current = self.head
            count = 0
            while current:
                if count == index:
                    return current
                count += 1
                current = current.next
        else:
            current = self.tail
            count = self.length - 1
            while current: 
                if count == index: 
                    return current
                count -= 1
                current = current.prev

        return current

    def set(self, index, val):
        updatedNode = self.get(index)
        if updatedNode is not None:
            updatedNode.val = val
            return True
        return False

    def insert(self, index, val) -> bool:
        if index < 0 or index > self.length - 1:
            return False
        if index == 0: 
            return ~~self.unshift(val)
        if index == self.length - 1: 
            return ~~self.push(val)
        
        newNode = ListNode(val)
        prevNode = self.get(index - 1)
        nextNode = prevNode.next

        prevNode.next = newNode
        newNode.prev = prevNode
        newNode.next = nextNode
        nextNode.prev = newNode
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length - 1:
            return False
        if index == 0:
            return self.shift()
        if index == self.length - 1:
            return self.pop()

        removeNode = self.get(index)

        prevNode = removeNode.prev
        nextNode = removeNode.next
        removeNode.prev = None
        removeNode.next = None
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
        self.length -= 1
        return removeNode

    def reverse(self):
        if self.head is None:
            return None

        temp = self.head
        self.head = self.tail
        self.tail = temp

        nextNode = None
        prevNode = None

        for i in range(self.length - 1):
            nextNode = temp.next
            temp.next = prevNode
            temp.prev = nextNode
            prevNode = temp
            temp = nextNode

        return self



    
# create new instance of DoublyLinkedList
DLL = DoublyLinkedList()

# push elements to the list
DLL.push(1)
DLL.push(2)
DLL.push(3)
DLL.push(4)
DLL.push(5)

# print the list
DLL.print_list()
# Output: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> None

# use the pop method to remove the last element and print its value
print(DLL.pop().val) # prints 5

# print the list after pop
DLL.print_list()
# Output: 1 <-> 2 <-> 3 <-> 4 <-> None

# use the shift method to remove the first element and print its value
print(DLL.shift().val) # prints 1

# print the list after shift
DLL.print_list()
# Output: 2 <-> 3 <-> 4 <-> None

# use the unshift method to add an element to the beginning of the list
DLL.unshift(0)

# print the list after unshift
DLL.print_list()
# Output: 0 <-> 2 <-> 3 <-> 4 <-> None

# use the get method to get an element at a specific index
print(DLL.get(1).val) # prints 2

# use the set method to update an element at a specific index
DLL.set(2, 10)

# print the list after updating an element
DLL.print_list()
# Output: 0 <-> 2 <-> 10 <-> 4 <-> None

# use the insert method to insert an element at a specific index
DLL.insert(2, 20)

# print the list after inserting an element
DLL.print_list()
# Output: 0 <-> 2 <-> 20 <-> 10 <-> 4 <-> None

# use the remove method to remove an element at a specific index
DLL.remove(2)

# print the list after removing an element
DLL.print_list()
# Output: 0 <-> 2 <-> 10 <-> 4 <-> None









