# 4 - https://leetcode.com/problems/median-of-two-sorted-arrays/

# Time: O(log(min(n, m))) where n and m are the lengths of the two arrays.
# Space: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # A will be the array with fewer elements
        if len(B) < len(A):
            A, B = B, A

        total = len(nums1) + len(nums2)
        half = total // 2
        left = 0
        right = len(A) - 1

        while True:
            AIndex = (left + right) // 2
            BIndex = half - AIndex - 2

            Aleft = A[AIndex] if AIndex >= 0 else float("-infinity")
            Aright = A[AIndex + 1] if AIndex + 1 < len(A) else float("infinity")
            Bleft = B[BIndex] if BIndex >= 0 else float("-infinity")
            Bright = B[BIndex + 1] if BIndex + 1 < len(B) else float("infinity")

            # left partition found, means we will know the median
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    # odd number of elements
                    return min(Aright, Bright)
                else:
                    # even number of elements
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = AIndex - 1
            elif Bleft > Aright:
                left = AIndex + 1