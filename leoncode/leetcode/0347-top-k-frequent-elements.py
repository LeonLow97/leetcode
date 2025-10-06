# 347 - https://leetcode.com/problems/top-k-frequent-elements/

# Time: O(N)
# Space: O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        numToCount = {}
        for num in nums:
            numToCount[num] = 1 + numToCount.get(num, 0)
        
        for num, count in numToCount.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            bucket = buckets[i]
            for item in bucket:
                res.append(item)
                if len(res) == k:
                    return res
        return res