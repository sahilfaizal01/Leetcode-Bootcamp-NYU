# using an extra prefix array
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 10000
        max_prof = 0
        min_pref = []
        for p in prices:
            if p < min_val:
                min_val = p
            min_pref.append(min_val)
        for p,m in zip(min_pref,prices):
            if m - p > max_prof:
                max_prof = m - p
        return max_prof
