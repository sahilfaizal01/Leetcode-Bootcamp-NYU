class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxs = []
        for i in range(len(nums)-k+1):
            maxv = max(nums[i:i+k])
            maxs.append(maxv)
        return maxs
