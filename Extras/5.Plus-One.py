# in-efficient solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = 0
        idx = 0
        for p in range(n-1,-1,-1):
            num += digits[idx]*(10**p)
            idx+=1
        num+=1
        res = []
        temp = str(num)
        for c in temp:
            res.append(int(c))
        return res
