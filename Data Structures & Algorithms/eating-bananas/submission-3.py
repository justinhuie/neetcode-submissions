class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We can use binary search to find the smallest k value
        # Calculate hours using math.ceil(p / k)
        # Let l = 1 and r = max(piles) since maximum number is highrest # of bananas

        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
            

