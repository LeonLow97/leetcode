'''
Difficulty: MEDIUM
No.1041    https://leetcode.com/problems/robot-bounded-in-circle/

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
'''

# My Solution
# Runtime: 35ms, Memory: 13.9 MB
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        n = len(instructions)

        # base case
        if n == 1: return False

        # Store the x-axis and y-axis in an array
        loc = [0, 0]
        current = "North"

        # repeat instructions 4 times
        instructions += instructions + instructions + instructions

        # iterate through the instructions
        for step in instructions:
            current = self.getDirection(current, step)
            if step == "G":
                print(loc)
                if current == "North": loc[1] += 1
                elif current == "South": loc[1] -= 1
                elif current == "East": loc[0] += 1
                elif current == "West": loc[0] -= 1
            
        if loc == [0,0]: return True

        return False

    def getDirection(self, current, step) -> str:
        if current == "North":
            if step == "G": return "North"
            elif step == "L": return "West"
            elif step == "R": return "East"
        elif current == "East":
            if step == "G": return "East"
            elif step == "L": return "North"
            elif step == "R": return "South"
        elif current == "West":
            if step == "G": return "West"
            elif step == "L": return "South"
            elif step == "R": return "North"
        elif current == "South":
            if step == "G": return "South"
            elif step == "L": return "East"
            elif step == "R": return "West"


S = Solution()
instructions = "GGLLGG"
print(S.isRobotBounded(instructions)) # True
instructions = "GG"
print(S.isRobotBounded(instructions)) # False
instructions = "GL"
print(S.isRobotBounded(instructions)) # True
instructions = "GLGLGGLGL"
print(S.isRobotBounded(instructions)) # False

# Eric's Solution
# Runtime: 30ms, Memory: 14 MB
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
        # if pos is row, col = 0, 0, return True
        if not posChanged:
            return True
        if curDirection != self.ORIGIN_DIRECTION: # result position must change
            return True
        
        return False


S = Solution()
instructions = "GGLLGG"
print(S.isRobotBounded(instructions)) # True
instructions = "GG"
print(S.isRobotBounded(instructions)) # False
instructions = "GL"
print(S.isRobotBounded(instructions)) # True
instructions = "GLGLGGLGL"
print(S.isRobotBounded(instructions)) # False   
