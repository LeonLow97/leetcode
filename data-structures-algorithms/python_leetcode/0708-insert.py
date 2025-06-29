'''
Difficulty: MEDIUM
No.708    https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

https://blog.csdn.net/hgq522/article/details/122356606

Given a Circular Linked List node, which is sorted in ascending order, write a function to 
insert a value  insertVal into the list such that it remains a sorted circular list. The given 
node can be a reference to any single node in the list and may not Necessarily be the smallest 
value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. 
After the insertion, the circular list should remain sorted.

If the list is empty (ie, the given node is  null), you should create a new single circular list 
and return the reference to that single node. Otherwise, you should return the originally given node.

Constraints:

The number of nodes in the list is in the range  [0, 5 * 10^4].
-10^6 <= Node.val, insertVal <= 10^6
'''



