class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        
        for person in range(1, n + 1):
            if indegree[person] == n - 1 and outdegree[person] == 0:
                return person

        return -1
        
        # for each node, check
        # if outdegree of node is n-1 and indegree is 0 then
        # easier to check if there exists someone who trusts everyone
        # and no one trusts judge
        # outdegree(judge) = n - 1
        # indegree(judge) = 0
        # if these two conditions are satisfied then we have a judge and we return this node
