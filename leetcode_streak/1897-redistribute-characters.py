# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/?envType=daily-question&envId=2023-12-30

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = {}
        
        for word in words:
            for c in word:
                counts[c] = counts.get(c, 0) + 1
        
        n = len(words)
        for val in counts.values():
            if val % n != 0:
                return False
        
        return True
