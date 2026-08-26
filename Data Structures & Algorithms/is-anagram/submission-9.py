class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Edge cases to consider
        # Number of characters are not the same 
        # The exact same character count 
        # Multiple of the same character

        if len(t) != len(s):
            return False

        charsS = {}
        charsT = {}

        for i in range(len(s)):
            charsS[s[i]] = charsS.get(s[i], 0) + 1
            charsT[t[i]] = charsT.get(t[i], 0) + 1
        
        for c in charsS:
            if charsS.get(c) != charsT.get(c):
                return False
        
        return True