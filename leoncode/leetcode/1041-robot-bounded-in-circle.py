# 1041 - https://leetcode.com/problems/robot-bounded-in-circle/

# Time: O(n)
# Space: O(1)

class Solution:
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3
    ORIGIN_DIRECTION = UP
    
    def isRobotBounded(self, instructions: str) -> bool:
        curDirection = self.ORIGIN_DIRECTION
        row, col = 0, 0
        
        for curChar in instructions:
            if curChar == 'G':
                if curDirection == self.UP:
                    row -= 1
                elif curDirection == self.DOWN:
                    row += 1
                elif curDirection == self.LEFT:
                    col -= 1
                elif curDirection == self.RIGHT:
                    col += 1
            elif curChar == 'L':
                curDirection = (curDirection + 1) % 4
            elif curChar == 'R':
                curDirection = (curDirection - 1) % 4
                
        posChanged = row != 0 or col != 0
        if not posChanged:
            return True
        if curDirection != self.ORIGIN_DIRECTION:
            return True
        
        return False