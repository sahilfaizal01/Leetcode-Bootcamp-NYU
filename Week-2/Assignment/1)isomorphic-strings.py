class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for c1,c2 in zip(s,t):
            X = (c1 in s_map and s_map[c1]!=c2)
            Y = (c2 in t_map and t_map[c2]!=c1)
            if(X or Y):
                return False
            s_map[c1] = c2
            t_map[c2] = c1
        return True
