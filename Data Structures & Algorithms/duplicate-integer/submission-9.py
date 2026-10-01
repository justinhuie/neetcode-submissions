class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for n in nums:
            if n not in duplicate:
                duplicate.add(n)
            else:
                return True
        return False
