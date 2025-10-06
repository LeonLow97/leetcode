# 416 - https://leetcode.com/problems/partition-equal-subset-sum/

# Time: O(n * target) where n is number of elements in nums, target is sum(nums) // 2
# Space: O(target) for dp set

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)

        ## if sumNums is odd, impossible to get a partition of 2 equal sum subsets
        if sumNums % 2 == 1: return False

        target = sumNums // 2

        ## define dp set
        dp = set()
        dp.add(0) # add '0' because we can either include the number or exclude

        for num in nums:
            # initialize tempDP because we are iterating over dp below
            # don't want to add new elems to dp will iterating over it
            tempDP = set()
            for t in dp:
                # optimization, once we found target, return True
                if num + t == target: return True
                
                tempDP.add(t + num)
                tempDP.add(t)
            
            dp = tempDP

        # return True if target in dp else False
        return False