# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_pointer = 0 
        last_pointer = len(numbers) - 1

        while start_pointer != last_pointer:
            sumOfTarget = numbers[start_pointer] + numbers[last_pointer]
            if sumOfTarget == target:
                return  [start_pointer + 1, last_pointer + 1]
            elif sumOfTarget > target:
                last_pointer -= 1
            else:
                start_pointer += 1
