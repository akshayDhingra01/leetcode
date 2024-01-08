class Solution:
    def isValid(self, s: str) -> bool:
        bracs_dict = {
            "(" : ")" , "{" :  "}"  , "[" : "]"
        }
        stack = []

        for element in s:
            if element in bracs_dict:
                stack.append(element)
                continue
            if not stack or bracs_dict[stack[-1]] != element:
                return False
            stack.pop()

        return not stack


