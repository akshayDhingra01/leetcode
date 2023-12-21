# Question https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lengthOfList = len(nums)
        lengthOfSet = len(set(nums))
        if (lengthOfSet < lengthOfList):
            return True
        else:
            return False