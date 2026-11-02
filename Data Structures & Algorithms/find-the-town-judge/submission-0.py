class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        reverse = [[] for _ in range(n+1)]

        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)

        for a, b in trust:
            reverse[b].append(a)

        for a, b in enumerate(reverse):
            outdegree[a] = len(b)
            for reverse_trust in b:
                indegree[reverse_trust] += 1
        
        for i in range(n+1):
            if indegree[i] == 0 and outdegree[i] == n-1:
                return i
        return -1
        
        # for each node, check
        # if outdegree of node is n-1 and indegree is 0 then
        # easier to check if there exists someone who trusts everyone
        # and no one trusts judge
        # outdegree(judge) = n - 1
        # indegree(judge) = 0
        # if these two conditions are satisfied then we have a judge and we return this node
