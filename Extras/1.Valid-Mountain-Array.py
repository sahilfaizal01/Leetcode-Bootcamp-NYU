class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        idx = 1
        while(idx<len(arr) and arr[idx]>arr[idx-1]):
            idx+=1
        if(idx==1 or idx==len(arr)):
            return False
        while(idx<len(arr) and arr[idx]<arr[idx-1]):
            idx+=1
        return idx==len(arr)
