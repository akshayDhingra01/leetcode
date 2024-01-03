# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left_pointer = 0
        long_substring_value = 0

        for right_index in range(len(s)):
            while s[right_index] in charSet:
                charSet.remove(s[left_pointer])
                left_pointer += 1
            charSet.add(s[right_index])
            long_substring_value = max(long_substring_value, right_index - left_pointer + 1)
        return long_substring_value
