class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weaker = set()
        for u,v in edges:
            weaker.add(v)
        teams = []
        for i in range(n):
            if i not in weaker:
                teams.append(i)
        return teams[0] if len(teams) == 1 else -1