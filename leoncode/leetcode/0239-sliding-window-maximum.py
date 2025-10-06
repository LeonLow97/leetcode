# 239 - https://leetcode.com/problems/sliding-window-maximum/

# Time: O(N)
# Space: O(K)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # top of queue stores the highest element in window

        left = 0

        for right in range(len(nums)):
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)

            # ensure top of queue's index is still valid, could be old index
            if q[0] < left:
                q.popleft()

            if right + 1 >= k:
                res.append(nums[q[0]])
                left += 1            

        return res