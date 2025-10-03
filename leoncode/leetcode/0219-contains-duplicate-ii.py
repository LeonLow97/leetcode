# 219 - https://leetcode.com/problems/contains-duplicate-ii/

# Optimal: Hash Map
# Time: O(n)
# Space: O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numToIdx = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in numToIdx and abs( i - numToIdx[num] ) <= k:
                return True
            numToIdx[num] = i

        return False

# Optimal: Sliding Window + Hash Set
# Time: O(n)
# Space: O(k) better space because we consider only unique elements
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        left = 0

        for right in range(len(nums)):
            num = nums[right]

            if abs(right - left) > k:
                seen.remove(nums[left])
                left += 1
            
            if num in seen:
                return True
            
            seen.add(num)
        
        return False