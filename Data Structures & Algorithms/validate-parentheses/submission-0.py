class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {
            "(": ")",
            "{": "}",
            "[": "]"
            }
        for parentheses in s:
            if parentheses in pMap.keys():
                stack.append(parentheses)   
            elif not stack or parentheses != pMap[stack.pop()]:
                return False

        return not stack


        