'''
Difficulty: Easy
No.203    https://leetcode.com/problems/remove-linked-list-elements/

Given the head of a linked list and an integer val, remove all the 
nodes of the linked list that has Node.val == val, and return the new head.

Constraints:

- The number of nodes in the list is in the range [0, 10^4].
- 1 <= Node.val <= 50
- 0 <= val <= 50
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # base case
        if head is None:
            return None
        
        # define pointers
        dummy = ListNode()
        dummy.next = head
        current = head
        previous = dummy
    
        # traverse the linked list
        while current is not None:
            if current.val == val:
                previous.next = current.next
                current = previous.next
            else:
                previous = current
                current = current.next

        # return head node
        return dummy.next

def create_linked_list(values):
    node = ListNode(values[0])
    head = node

    for value in values[1:]:
        node.next = ListNode(value)
        node = node.next

    return head

values1 = [1, 2, 6, 3, 4, 5, 6]
head1 = create_linked_list(values1)

values2 = [7, 7, 7, 7]
head2 = create_linked_list(values2)

result = Solution().removeElements(head1, 6)

while result:
    print(result.val, end = " -> ")
    result = result.next
print()

result = Solution().removeElements(head2, 7)

while result:
    print(result.val, end = " -> ")
    result = result.next


