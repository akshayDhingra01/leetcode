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
