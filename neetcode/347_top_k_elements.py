# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for number in nums:
            if number not in nums_dict.keys():
                nums_dict[number] = 1
            else:
                nums_dict[number] += 1

        nums_dict_sorted = sorted(nums_dict.items(), key=lambda x: x[1], reverse=False)
        print(nums_dict_sorted)
        return_array = []
        for key in nums_dict_sorted:
            return_array.append(key[0])
            if k == 0:
                break
            k -= 1
        if len(return_array) == 0:
            return nums
        return return_array