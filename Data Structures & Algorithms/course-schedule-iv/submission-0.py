class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        ancestors = [set() for _ in range(numCourses)]

        for a,b in prerequisites:
            adj[a].append(b)
            indegrees[b] += 1

        # find whether u comes before v

        q = deque([course for course in range(numCourses) if indegrees[course] == 0])

        # where if index of u comes before index of v then it is a prequisite course

        while q:
            course = q.popleft()
            
            for neighbor in adj[course]:
                ancestors[neighbor].add(course)
                ancestors[neighbor].update(ancestors[course])

                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    q.append(neighbor)

        return [u in ancestors[v] for u,v in queries]

