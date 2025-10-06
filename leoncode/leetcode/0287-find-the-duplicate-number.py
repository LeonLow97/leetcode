# 287 - https://leetcode.com/problems/find-the-duplicate-number/

# Time: O(n)
# Space: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Linked List Cycle problem (Floyd's algorithm)
        # the start of the cycle is the return value
        # watch neetcode video on this again, he said will forget so just rewatch

        # Indexes: 0,1,2,3,4
        #         [1,3,4,2,2] # elements in array are the indexes, e.g., both `2` will point to index 2
        # Notice that there will never be element 0 because of the range [1, n] so first element in
        # linked list is always 0

        slow, fast = 0, 0 # `0` index is never part of the cycle

        # finding where slow meets fast
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # move fast pointer 2 times
            if slow == fast:
                break

        # finding the beginning of the linked list cycle
        slow2 = 0 # initialize another pointer at the beginning of the linked list
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow # returning the index which is also the element