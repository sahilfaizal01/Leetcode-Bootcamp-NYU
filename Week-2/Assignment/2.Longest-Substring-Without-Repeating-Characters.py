# failing a single test-case
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        if len(s)==0:
            return 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substrings.append(s[i:j])
        unique_strs = []
        for substr in substrings:
            if len(substr) == len(set(substr)):
                unique_strs.append(substr)
        temp = sorted(unique_strs,key=(lambda x: len(x)),reverse=True)
        return len(temp[0])  
