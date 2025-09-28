# Fast and Slow Pointers

- [Python Fast and Slow Pointers](https://www.koderdojo.com/blog/detect-cycle-in-linked-list-using-floyd-s-cycle-finding-algorithm)
- [Fast and Slow Pointers Tutorial](https://iq.opengenus.org/fast-and-slow-pointer-technique/)

## Fast and Slow Pointer Technique (Linked List)

- Also known as Floyd's Cycle Detection Algorithm.
- Uses 2 pointers to determine traits about directional data structures. (can be array, singly-linked list, or a graph).
- Often used for **detecting a cycle in a linked list.**
- Slow pointer travels the linked list one node at a time whereas a fast pointer travels the linked list two nodes at a time.
  - This concept can be used in cases like detecting a loop in a graph, find the middle node of a linked list (better time complexity), flattening a linked list, etc.
- If these pointers ever point to the same node in the linked list, there is a cycle in the linked list.

## Algorithm Implementation

- Initially, the slow and fast pointers will point to the head of the linked list.
- With each iteration, the 2 pointers will be advanced at different rates.
- Usually, the slow pointer will move ahead 1 step while the fast pointer moves ahead 2.
- Then, compare the pointers to see if they are pointing to the same node.
  - If they are, return `True`. Else, return `False`.

```py
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

## Problem 1: Middle of Linked List

- Time Complexity: O(N)
- slow = slow + 1 => slow = slow.next
- fast = fast + 2 => fast = fast.next.next
