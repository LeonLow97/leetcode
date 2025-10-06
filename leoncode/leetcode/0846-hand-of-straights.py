# 846 - https://leetcode.com/problems/hand-of-straights/

# Time: O(n log n)
# Space: O(n)

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hashMap = {}
        for h in hand:
            if h not in hashMap:
                hashMap[h] = 0
            hashMap[h] += 1
    
        minHeap = list(hashMap.keys())
        heapq.heapify(minHeap) # O(n)

        while minHeap:
            minVal = minHeap[0]

            for num in range(minVal, minVal + groupSize):
                if num not in hashMap or hashMap[num] == 0:
                    return False
                hashMap[num] -= 1
                if hashMap[num] == 0:
                    if num != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        
        return True
