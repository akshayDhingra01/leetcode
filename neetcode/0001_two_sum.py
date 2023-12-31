# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        start_pointer = 0
        end_pointer = len(nums) - 1
        while start_pointer < end_pointer :
            if nums_sorted[start_pointer] + nums_sorted[end_pointer] == target:
                if nums_sorted[start_pointer] == nums_sorted[end_pointer]:
                    return [nums.index(nums_sorted[start_pointer]), nums.index(nums_sorted[end_pointer],nums.index(nums_sorted[start_pointer]) + 1 )]
                return [nums.index(nums_sorted[start_pointer]), nums.index(nums_sorted[end_pointer])]
            elif nums_sorted[start_pointer] + nums_sorted[end_pointer] > target:
                end_pointer -= 1
            else:
                start_pointer += 1




# Other Approach
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
