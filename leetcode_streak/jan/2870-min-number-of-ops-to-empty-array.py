# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/?envType=daily-question&envId=2024-01-04

# First Solution: Time O(N) || Space O(N) || Dict

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hash_map = {}
        for number in nums:
            if number in hash_map.keys():
                hash_map[number] += 1
            else:
                hash_map[number] = 1
            
        print(hash_map)

        number_of_operations = 0

        for key, value in hash_map.items():
            if value == 1:
                return -1
            if value % 3 == 0:
                number_of_operations += (value / 3)
            elif value % 3 == 1:
                number_of_operations += ((value - 4) / 3) + 2 
            elif value % 3 == 2:
                number_of_operations += (value // 3) + 1
        
        return int(number_of_operations)