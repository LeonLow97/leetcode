# 881 - https://leetcode.com/problems/boats-to-save-people/

# Optimal: Two Pointers
# Time: O(n log n)
# Space: O(1)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # O(n log n)
        left, right = 0, len(people) - 1
        res = 0

        while left <= right:
            # Shift left pointer if 2 people can board
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1 # heaviest person always boards
            res += 1

        return res
