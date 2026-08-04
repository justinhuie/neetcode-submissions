class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max = 0 
        for n in nums:
            if n == 1:
                counter += 1
            else:
                counter = 0
            if counter > max:
                max = counter
            
            
        return max 

            

        