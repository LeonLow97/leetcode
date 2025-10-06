# 875 - https://leetcode.com/problems/koko-eating-bananas/

# Time: O(n log m) where n is the number of piles and m is the maximum number of bananas in a pile.
# Space: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        left, right = 1, maxPile
        res = maxPile

        while left <= right:
            middle = left + (right - left) // 2 # eating speed

            time = 0
            for pile in piles:
                time += math.ceil(pile / middle)

            if time > h:
                # eat faster
                left = middle + 1
            else:
                res = min(res, middle)
                right = middle - 1

        return res
