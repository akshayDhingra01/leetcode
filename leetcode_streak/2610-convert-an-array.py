# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/?envType=daily-question&envId=2024-01-02

# First Approach || Dict or HashMap || Time O(N2) || Space O(N)

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hash_map = {}
        for number in nums:
            if number not in hash_map.keys():
                hash_map[number] = 1
            else:
                hash_map[number] += 1
        sorted_dict = sorted(hash_map.items(), key=lambda x:x[1], reverse=True)
        first_value = sorted_dict[0][0]
        res = []
        for key, value in sorted_dict:
            for i in range(value):
                if key == first_value:
                    arr = [key]
                    res.append(arr)
                else:
                    res[i].append(key)
        return res 



    # class Solution:
    # def findMatrix(self, v: List[int]) -> List[List[int]]:
    #     um = {}
    #     for i in v:
    #         um[i] = um.get(i, 0) + 1
        
    #     ans = []
    #     while um:
    #         temp = []
    #         to_erase = []
    #         for f, s in um.items():
    #             temp.append(f)
    #             s -= 1
    #             if s == 0:
    #                 to_erase.append(f)
    #             um[f] = s
    #         ans.append(temp)
    #         for i in to_erase:
    #             del um[i]
    #     return ans


