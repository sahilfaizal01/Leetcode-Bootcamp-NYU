class Solution:
    def isPalindrome(self, s: str) -> bool:
       s = s.lower()

       modified_s = ''.join(char for char in s if char.isalnum())

       return modified_s == modified_s[::-1]
