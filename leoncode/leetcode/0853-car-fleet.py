# 853 - https://leetcode.com/problems/car-fleet/

# Time: O(n log n)
# Space: O(n)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort() # O(n log n), sort cars according to their position

        stack = []

        for i in range(len(position)-1, -1, -1):
            p, s = cars[i]
            dist = target - p
            time = dist / s

            if not stack:
                stack.append(time)
                continue
            
            if time > stack[-1]:
                stack.append(time)

        return len(stack)
