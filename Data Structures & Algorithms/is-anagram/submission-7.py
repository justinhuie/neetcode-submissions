class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmapS = {}
        hashmapT = {}

        for c in s:
            hashmapS[c] = 1 + hashmapS.get(c, 0)
        for c in t:
            hashmapT[c] = 1 + hashmapT.get(c, 0)
        
        return hashmapS == hashmapT
