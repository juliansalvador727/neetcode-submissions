class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        indegree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        topological_ordering = []

        q = deque([course for course in range(numCourses) if indegree[course] == 0])

        while q:
            course = q.popleft()
            topological_ordering.append(course)

            for neighbor in adj[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        
        return topological_ordering if len(topological_ordering) == numCourses else []