class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]

        indegree = [0] * numCourses

        topological_ordering = []

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        q = deque([node for node in range(numCourses) if indegree[node] == 0])

        while q:
            course = q.popleft()
            topological_ordering.append(course)

            for neighbor in adj[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return True if len(topological_ordering) == numCourses else False