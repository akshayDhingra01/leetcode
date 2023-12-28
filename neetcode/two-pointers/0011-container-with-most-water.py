# https://leetcode.com/problems/container-with-most-water/


# First Solution 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start_pointer = 0
        last_pointer = len(height) - 1
        max_area = 0
        def getMax(start_pointer, last_pointer):                
            max_area = 0
            if height[start_pointer] < height[last_pointer]:
                max_area = height[start_pointer] * (last_pointer - start_pointer)
            else:
                max_area = height[last_pointer] * (last_pointer - start_pointer)
            return max_area
        
        max_area = getMax(start_pointer, last_pointer)

        while last_pointer > start_pointer:
            currentMax = getMax(start_pointer, last_pointer)
            if max_area < currentMax:
                max_area = currentMax
            if height[start_pointer] < height[last_pointer]:                
                start_pointer += 1
            else:
                last_pointer -= 1
        
        return max_area