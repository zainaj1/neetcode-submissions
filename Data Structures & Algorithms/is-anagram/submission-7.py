class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Edge cases to consider
        # Number of characters are not the same 
        # The exact same character count 
        # Multiple of the same character

        if len(t) != len(s):
            return False

        chars = {}
        for c in s:
            chars[c] = 1 if c not in chars else chars[c] + 1 
        
        for c in t:
            if c not in chars:
                return False
            
            chars[c] -= 1
            
            if chars[c] == 0:
                chars.pop(c)
        
        return len(chars) == 0
        