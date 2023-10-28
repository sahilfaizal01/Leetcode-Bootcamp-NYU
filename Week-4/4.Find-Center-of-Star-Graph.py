class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = {}
        for a,b in edges:
            if a not in nodes:
                nodes[a] = 1
            else:
                nodes[a] += 1 
            if b not in nodes:
                nodes[b] = 1
            else:
                nodes[b] += 1
        for n in nodes:
            if nodes[n] == len(edges):
                return n
