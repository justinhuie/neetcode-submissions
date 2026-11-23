class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        count = {}
        res = 0
        maxF = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            while (r - L + 1) - maxF > k:
                count[s[L]] -= 1
                L += 1
            
            res = max(res, r - L + 1)
        
        return res

            
        