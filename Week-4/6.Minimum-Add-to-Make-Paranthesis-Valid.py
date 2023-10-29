class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            else: 
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
        print(stack)
        return len(stack)
                
        # res = 0
        # bal = 0
        # for char in s:
        #     if char == '(':
        #         bal+=1
        #     elif(bal<=0):
        #         res+=1
        #     else:
        #         bal-=1
        # return bal+res
