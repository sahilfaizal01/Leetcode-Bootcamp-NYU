class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        start = 0
        end = len(height)-1
        while start<end:
            maxarea = max(maxarea,min(height[start],height[end])*(end-start))
            if(height[start]>=height[end]):
                end-=1
            else:
                start+=1
        return maxarea
