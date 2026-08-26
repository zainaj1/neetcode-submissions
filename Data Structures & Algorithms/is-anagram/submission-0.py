class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Edge cases to consider
        # Number of characters are not the same 
        # The exact same character count 
        # Multiple of the same character

        characters = {}
        for char in s:
            if char in characters:
                characters[char] = characters[char] + 1
            else:
                characters[char] = 1

        for char in t:
            if char in characters:
                characters[char] = characters[char] - 1
                if characters[char] == 0:
                    characters.pop(char)
            else:
                return False
        
        return len(characters.keys()) == 0

        