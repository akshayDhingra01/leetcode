# question https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums_new = sort(nums)

        # for i in range(len(nums)):
        #     print(i)
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        nums_new = nums.copy()
            
        nums_new.sort()

        a_index = 0
        b_index = len(nums) - 1

        while True:
            z = nums_new[a_index] + nums_new[b_index] 
            if z == target:
                if nums.index(nums_new[a_index]) == nums.index(nums_new[b_index]):
                    return [nums.index(nums_new[a_index]) , nums.index(nums_new[b_index] ,nums.index(nums_new[a_index]) + 1 )   ]
                return [ nums.index(nums_new[a_index]) , nums.index(nums_new[b_index])]
            elif z < target:
                a_index += 1
            elif z > target:
                b_index -= 1