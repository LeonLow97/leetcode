# 88 - https://leetcode.com/problems/merge-sorted-array/

# Optimal: Two Pointers from the end
# Time: O(m+n)
# Space: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x, y = m-1, n-1

        for z in range(m+n-1, -1, -1):
            # Out of bounds
            if x < 0:
                nums1[z] = nums2[y]
                y -= 1
                continue
            elif y < 0:
                break

            # Comparison, pick bigger number
            if nums1[x] >= nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            else:
                nums1[z] = nums2[y]
                y -= 1
