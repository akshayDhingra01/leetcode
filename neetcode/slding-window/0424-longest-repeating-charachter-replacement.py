# https://leetcode.com/problems/longest-repeating-character-replacement/

# First Solution || Time O(N2) || Space O(1) || Two Pointers || Sliding window

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        str_set = set()
        for char in s:
            str_set.add(char)
        max_count = 0

        if k == 0:
            local_sum = 1
            for index in range(1,len(s)):
                if s[index] == s[index-1]:
                    local_sum += 1 
                else:
                    max_count = max(max_count ,local_sum)
                max_count = max(max_count ,local_sum)
            return max_count

        
        for element in str_set:
            t = k
            str_max = ''

            for element2 in s:
                if element2 == element:
                    str_max += element2
                else:
                    if t!= 0:
                        str_max += element2
                        t -= 1
                    else:
                        for index in range(len(str_max)):
                            if str_max[index] != element:
                                str_max = str_max[index + 1:] + element2
                                break
                    
                max_count = max(max_count ,len(str_max))
        return max_count