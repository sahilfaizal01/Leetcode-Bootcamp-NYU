class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #O(N)
        #using sets
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False
        #using hashMap (more time efficient than using set function)
        hashMap = {}
        for n in nums:
            if n in hashMap:
                return True
            hashMap[n] = 1
        return False
        #-------------------------------------------------------------
        #O(N Log N)
        #using sorting operation (more memory efficient)
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                return True
        return False

        
