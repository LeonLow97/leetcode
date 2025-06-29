'''
Difficulty: MEDIUM
No.11    https://leetcode.com/problems/container-with-most-water/
'''

def maxArea(height):
    if (len(height) == 2): return min(height)

    left = 0;
    right = len(height) - 1
    area = 0

    while (left < right):
        minHeight = min(height[left], height[right])
        width = right - left
        currentArea = minHeight * width
        if (currentArea > area):
            area = currentArea
        else:
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
    
    return area

print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1])) # 1
        

