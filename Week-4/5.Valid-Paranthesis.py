class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {'}':'{',']':'[',')':'('}
        
        for char in s:
            if char in lookup.values():
                stack.append(char)
            elif stack and lookup[char] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return stack == []
