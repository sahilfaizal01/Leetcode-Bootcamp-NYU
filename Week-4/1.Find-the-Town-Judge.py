class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if(len(trust) < n-1):
            return -1
        # using two arrays
        out_degree = [0] * (n+1)
        in_degree = [0] * (n+1)
        for a,b in trust:
            out_degree[a] += 1
            in_degree[b] += 1
        for i in range(1,n+1):
            if out_degree[i] == 0 and in_degree[i] == n-1:
                return i
        return -1

        # using one array
        # temp = [0] * (n+1)
        # for a,b in trust:
        #     temp[a] -= 1
        #     temp[b] += 1
        # print(temp)
        # for i, score in enumerate(temp[1:],1):
        #     print(i,score)
        #     if score == n-1:
        #         return i
        # return -1      
