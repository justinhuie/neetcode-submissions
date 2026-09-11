class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for s in magazine:
            hashmap[ord(s)] = 1 + hashmap.get(ord(s), 0)
        for s in ransomNote:
            letter = ord(s)
            if hashmap.get(letter, 0) > 0:
                hashmap[ord(s)] -= 1 
            else:
                return False
        return True
        