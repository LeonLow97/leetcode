# 0912 - https://leetcode.com/problems/sort-an-array/

# Time: O(n log n) - we are dividing the array in half each time (log n) and merging them back together (n)
# Space: O(n) - we are using extra space to store the left and right arrays

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        # Merge Sort
        # divide
        midpoint = len(nums) // 2
        left_arr = nums[:midpoint]
        right_arr = nums[midpoint:]

        self.sortArray(left_arr)
        self.sortArray(right_arr)

        # conquer
        l, r, i = 0, 0, 0
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                nums[i] = left_arr[l]
                l += 1
            else:
                nums[i] = right_arr[r]
                r += 1
            i += 1
        
        # could have some elements left either left arr or right arr
        while l < len(left_arr):
            nums[i] = left_arr[l]
            l += 1
            i += 1
        
        while r < len(right_arr):
            nums[i] = right_arr[r]
            r += 1
            i += 1
        
        return nums