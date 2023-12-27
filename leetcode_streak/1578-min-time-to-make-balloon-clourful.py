# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


# First Solution: Time O(N) || Space O(N) || Dict
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        def getMinOfArray(value):
            min_array = []
            for number in value:
                min_array.append(neededTime[number])
            max_element = max(min_array)
            min_array.remove(max_element)
            return sum(min_array)

        ballons_dict = {}

        for index in range(len(colors)):
            ballon = colors[index]
            if ballon in ballons_dict.keys():
                ballons_dict[ballon].append(index)
            else:
                ballons_dict[ballon] = [index]

        ballons_to_remove = []
        ballons_to_remove_time = []

        for key, value in ballons_dict.items():
            if len(value) == 1:
                continue
            first_item = value[0]
            local_array = [value[0]]

            for index_of_array in range(1, len(value)):
                if value[index_of_array] - 1 == first_item:
                    local_array.append(value[index_of_array])
                else:
                    ballons_to_remove.append(local_array)
                    local_array = [value[index_of_array]]
                first_item = value[index_of_array]
            ballons_to_remove.append(local_array)

        ans = 0
        # print(ballons_to_remove)
        for element_array in ballons_to_remove:
            if len(element_array) == 1 or len(element_array) == 0:
                continue
            ans += getMinOfArray(element_array)

        return ans
