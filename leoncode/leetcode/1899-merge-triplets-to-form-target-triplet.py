# 1899 - https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

# Time: O(n)
# Space: O(1)

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        goodIndices = set()

        for triplet in triplets:
            # check if any number in current triplet is greater than target
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            # loop through triplet and check if any value is equal to target, save that index
            for i in range(3):
                if triplet[i] == target[i]:
                    goodIndices.add(i)

        return len(goodIndices) == 3
