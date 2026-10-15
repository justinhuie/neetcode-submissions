class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        runningSum = 0

        while l < r:
            volume = (r - l) * min(heights[l], heights[r])
            if volume > runningSum:
                runningSum = volume
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r-= 1
        return runningSum


        